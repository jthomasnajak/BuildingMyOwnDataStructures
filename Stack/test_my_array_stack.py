# ----------------------------------------
# My Array Stack Unit Testing
# 2022-08-14
# ----------------------------------------
# Goal:
# Implement a Stack stored as an array
# desired functions:
# push(Value) - pushes value to top of stack
# top() - returns value at top of stack
# pop() - removes and returns value at top of stack
# empty() - returns true if stack is empty

import my_array_stack

# should push value to top of stack
def test_my_array_stack_push():
    test_array_stack = my_array_stack.my_array_stack()
    test_array_stack.push(5)
    test_array_stack.push(10)
    assert test_array_stack.pop() == 10
    assert test_array_stack.pop() == 5

# should return value at top of stack
def test_my_array_stack_top():
    test_array_stack = my_array_stack.my_array_stack()
    test_array_stack.push(5)
    assert test_array_stack.top() == 5
    assert test_array_stack.top() == 5

# should remove and return value at top of stack
def test_my_array_stack_pop():
    test_array_stack = my_array_stack.my_array_stack()
    test_array_stack.push(5)
    test_array_stack.push(10)
    assert test_array_stack.pop() == 10
    assert test_array_stack.pop() == 5

# should return true if empty and false if a value is contained
def test_my_array_stack_empty():
    test_array_stack = my_array_stack.my_array_stack()
    assert test_array_stack.empty() == True
    test_array_stack.push(1)
    assert test_array_stack.empty() == False