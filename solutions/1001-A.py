'''
Problem id: 1001-A
Statement: You are given a qubit in state  and an integer sign. 

Your task is to convert the given qubit to state  if sign = 1 or  if sign =  - 1.

You have to implement an operation which takes a qubit and an integer as an input and has no output. The "output" of your solution is the state in which it left the input qubit.

Your code should have the following signature:
Tags: *specialproblem,*1100
'''

class Qubit:
    def __init__(self, state='|0⟩'):
        self.state = state

    def __str__(self):
        return self.state


def transform_qubit(qubit, sign):
    if sign == 1:
        qubit.state = '|0⟩'  # Set state to |0⟩
    elif sign == -1:
        qubit.state = '|1⟩'  # Set state to |1⟩
    else:
        print("Unexpected sign value. Expected 1 or -1.")

# Verification function
def verify_transformation(initial_state, sign, expected_state):
    qubit = Qubit(initial_state)
    transform_qubit(qubit, sign)
    actual_state = str(qubit)
    if actual_state == expected_state:
        print('verified')
    else:
        print(f'Incorrect transformation. Actual: {actual_state}, Expected: {expected_state}')

# Test the function
verify_transformation('|0⟩', 1, '|0⟩')  # Should print 'verified'
verify_transformation('|1⟩', -1, '|1⟩')  # Should print 'verified'
verify_transformation('|0⟩', -1, '|1⟩')  # Should print 'verified'
verify_transformation('|1⟩', 1, '|0⟩')  # Should print 'verified'
verify_transformation('|0⟩', 0, '|0⟩')  # Should print "Unexpected sign value..." and "Incorrect transformation..."