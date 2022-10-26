# ----------------------------------------
# My List Stack Unit Testing
# 2022-08-17
# ----------------------------------------
# Goal:
# Implement a Stack stored as an list
# desired functions:
# push(Value) - pushes value to top of stack
# top() - returns value at top of stack
# pop() - removes and returns value at top of stack
# empty() - returns true if stack is empty

import my_list_stack

# should push value to top of stack
def test_my_list_stack_push():
    test_list_stack = my_list_stack.my_list_stack()
    test_list_stack.push(5)
    test_list_stack.push(10)
    assert test_list_stack.pop() == 10
    assert test_list_stack.pop() == 5

# should return value at top of stack
def test_my_list_stack_top():
    test_list_stack = my_list_stack.my_list_stack()
    test_list_stack.push(5)
    assert test_list_stack.top() == 5
    assert test_list_stack.top() == 5

# should remove and return value at top of stack
def test_my_list_stack_pop():
    test_list_stack = my_list_stack.my_list_stack()
    test_list_stack.push(5)
    test_list_stack.push(10)
    assert test_list_stack.pop() == 10
    assert test_list_stack.pop() == 5

# should return true if empty and false if a value is contained
def test_my_list_stack_empty():
    test_list_stack = my_list_stack.my_list_stack()
    assert test_list_stack.empty() == True
    test_list_stack.push(1)
    assert test_list_stack.empty() == False