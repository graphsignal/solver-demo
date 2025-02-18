'''
Problem id: 10-B
Statement: All cinema halls in Berland are rectangles with K rows of K seats each, and K is an odd number. Rows and seats are numbered from 1 to K. For safety reasons people, who come to the box office to buy tickets, are not allowed to choose seats themselves. Formerly the choice was made by a cashier, but now this is the responsibility of a special seating program. It was found out that the large majority of Berland's inhabitants go to the cinema in order to watch a movie, that's why they want to sit as close to the hall center as possible. Moreover, a company of M people, who come to watch a movie, want necessarily to occupy M successive seats in one row. Let's formulate the algorithm, according to which the program chooses seats and sells tickets. As the request for M seats comes, the program should determine the row number x and the segment [yl, yr] of the seats numbers in this row, where yr - yl + 1 = M. From all such possible variants as a final result the program should choose the one with the minimum function value of total seats remoteness from the center. Say,  — the row and the seat numbers of the most "central" seat. Then the function value of seats remoteness from the hall center is . If the amount of minimum function values is more than one, the program should choose the one that is closer to the screen (i.e. the row number x is lower). If the variants are still multiple, it should choose the one with the minimum yl. If you did not get yet, your task is to simulate the work of this program. 

The first line contains two integers N and K (1 ≤ N ≤ 1000, 1 ≤ K ≤ 99) — the amount of requests and the hall size respectively. The second line contains N space-separated integers Mi from the range [1, K] — requests to the program.

Output N lines. In the i-th line output «-1» (without quotes), if it is impossible to find Mi successive seats in one row, otherwise output three numbers x, yl, yr. Separate the numbers with a space.
Tags: dp,implementation,*1500
'''

# Solution implementation based on step-by-step plan
def solution(N, K, requests):
    # Initialize the cinema hall
    cinema_hall = [[False] * K for _ in range(K)]
    
    # Calculate the center position of the hall
    center_row, center_seat = (K + 1) // 2, (K + 1) // 2
    
    # Results list
    results = []
    
    # Process each request
    for party_size in requests:
        min_distance = float('inf')
        best_row, best_yl = -1, -1
        
        # Iterate over each row
        for x in range(K):
            # Try to find a block of `party_size` consecutive seats
            for yl in range(K - party_size + 1):
                yr = yl + party_size - 1
                
                # Check if the block is unoccupied
                if all(not cinema_hall[x][j] for j in range(yl, yr + 1)):
                    # Calculate remoteness from the center
                    remoteness = sum((x + 1 - center_row) ** 2 + (j + 1 - center_seat) ** 2 for j in range(yl, yr + 1))
                    
                    # Check if this is the best option
                    if (remoteness < min_distance or
                        (remoteness == min_distance and x < best_row) or
                        (remoteness == min_distance and x == best_row and yl < best_yl)):
                        min_distance = remoteness
                        best_row, best_yl = x, yl
        
        # If we found a suitable block, occupy it
        if min_distance < float('inf'):
            # Mark the seats as occupied
            for j in range(best_yl, best_yl + party_size):
                cinema_hall[best_row][j] = True
            # Append result as 1-based index
            results.append((best_row + 1, best_yl + 1, best_yl + party_size))
        else:
            results.append(-1)
    
    return results

def verify_solution():
    # Test case: hall 3x3, 2 requests of sizes 1 and 2
    N_test, K_test = 2, 3
    requests_test = [1, 2]
    expected_output = [(2, 2, 2), (1, 1, 2)]
    
    actual_output = solution(N_test, K_test, requests_test)
    
    if actual_output == expected_output:
        print("verified")
    else:
        print(
            f"verification failed - Expected: {expected_output}, Actual: {actual_output}"
        )

verify_solution()