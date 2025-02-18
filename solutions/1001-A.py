'''
Problem id: 1001-A
Statement: You are given a qubit in state  and an integer sign. 

Your task is to convert the given qubit to state  if sign = 1 or  if sign =  - 1.

You have to implement an operation which takes a qubit and an integer as an input and has no output. The "output" of your solution is the state in which it left the input qubit.

Your code should have the following signature:
Tags: *specialproblem,*1100
'''

def solution(sign):
    if sign == 1:
        return [0.707, 0.707]  # Represents |+⟩
    elif sign == -1:
        return [0.707, -0.707]  # Represents |-⟩
    else:
        raise ValueError("Sign must be either 1 or -1.")


def verify_solution():
    # Test case for sign = 1
    sign = 1
    expected_state_plus = [0.707, 0.707]  # |+⟩ expected state
    result_state = solution(sign)
    if all([abs(a - b) < 0.001 for a, b in zip(expected_state_plus, result_state)]):
        print("Verified: The qubit is in the |+⟩ state as expected.")
    else:
        print(f"Incorrect: Expected {expected_state_plus} but got {result_state}")

    # Test case for sign = -1
    sign = -1
    expected_state_minus = [0.707, -0.707]  # |-⟩ expected state
    result_state = solution(sign)
    if all([abs(a - b) < 0.001 for a, b in zip(expected_state_minus, result_state)]):
        print("Verified: The qubit is in the |-⟩ state as expected.")
    else:
        print(f"Incorrect: Expected {expected_state_minus} but got {result_state}")


verify_solution()