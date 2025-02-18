'''
Problem id: 100-H
Statement: Do you know the game Battleship? If no, look into Wikipedia article http://en.wikipedia.org/wiki/Battleship_(game). You are given the positions of ships on a 10 × 10 board for playing Battleship. According to the rules, the board should contain the following ships: 

The ships should not 'bend', touch each other or overlap in any way. Each ship can be oriented horizontaly or verticaly. Your task is to check whether the given set of boards meets the given conditions.

The first line contains number n (1 ≤ n ≤ 10) — the number of boards. Each board is described by 10 lines containing 10 characters each. The symbol "0" stands for an empty square and the symbol "*" stands for a square occupied by a ship. The descriptions of boards are separated with empty lines.

Print n lines YES or NO. Print the first word if the board meets the given conditions; otherwise print the second word.
Tags: *specialproblem,dfsandsimilar,implementation,*2100
'''

def is_valid_battleship_board(board):
    expected_ship_counts = {4: 1, 3: 2, 2: 3, 1: 4}
    visited = [[False] * 10 for _ in range(10)]
    actual_ship_counts = {1: 0, 2: 0, 3: 0, 4: 0}

    directions = [(0, 1), (1, 0)]  # Right, Down

    def dfs(r, c):
        stack = [(r, c)]
        cells = []
        visited[r][c] = True
        while stack:
            x, y = stack.pop()
            cells.append((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 10 and 0 <= ny < 10 and not visited[nx][ny] and board[nx][ny] == '*':
                    if (nx == x or ny == y):  # only allow straight lines
                        visited[nx][ny] = True
                        stack.append((nx, ny))
        return cells

    for i in range(10):
        for j in range(10):
            if board[i][j] == '*' and not visited[i][j]:
                ship_cells = dfs(i, j)
                if len(ship_cells) > 4:
                    return "NO"  # Ship is too large
                # Check if the ship "bends" or is touching another
                if all(x == ship_cells[0][0] for x, y in ship_cells):
                    # Entirely horizontal
                    row = ship_cells[0][0]
                    for y in range(min(y for x, y in ship_cells), max(y for x, y in ship_cells) + 1):
                        if board[row][y] != '*':
                            return "NO"  # Bent ship or gap
                        if any((row - 1 >= 0 and board[row - 1][y] == '*') or (row + 1 < 10 and board[row + 1][y] == '*') for y in range(min(y for x, y in ship_cells), max(y for x, y in ship_cells) + 1)):
                            return "NO"
                elif all(y == ship_cells[0][1] for x, y in ship_cells):
                    # Entirely vertical
                    col = ship_cells[0][1]
                    for x in range(min(x for x, y in ship_cells), max(x for x, y in ship_cells) + 1):
                        if board[x][col] != '*':
                            return "NO"  # Bent ship or gap
                        if any((col - 1 >= 0 and board[x][col - 1] == '*') or (col + 1 < 10 and board[x][col + 1] == '*') for x in range(min(x for x, y in ship_cells), max(x for x, y in ship_cells) + 1)):
                            return "NO"
                else:
                    return "NO"  # Bent ship

                actual_ship_counts[len(ship_cells)] += 1

    if actual_ship_counts == expected_ship_counts:
        return "YES"
    else:
        return "NO"


def solution(boards):
    results = []
    for board in boards:
        results.append(is_valid_battleship_board(board))
    return results


def test_solution():
    boards = [
        [
            "****000000",
            "0000000000",
            "0000***000",
            "0000000000",
            "00**000000",
            "0000000000",
            "0**0000000",
            "0000000000",
            "*000000000",
            "000000000*"
        ],
        [
            "****000000",
            "0000000000",
            "0000***000",
            "0000000000",
            "00**000**0",
            "0000000000",
            "0**0000000",
            "0000000000",
            "*000000000",
            "000000000*"
        ],
        [
            "****000000",
            "000000*000",
            "0000***000",
            "0000000000",
            "00**000000",
            "0000000000",
            "0**0000000",
            "0000000000",
            "*000000000",
            "000000000*"
        ],
        [
            "****000000",
            "0000000000",
            "0000***000",
            "0000000000",
            "00**0**000",
            "0000000000",
            "0**0000000",
            "0000000000",
            "*000000000",
            "000000000*"
        ]
    ]
    expected = ["YES", "NO", "NO", "NO"]
    results = solution(boards)
    for i, (result, exp) in enumerate(zip(results, expected)):
        if result == exp:
            print(f"Test Case {i + 1}: verified")
        else:
            print(f"Test Case {i + 1}: incorrect. Got {result}, expected {exp}")

test_solution()