# ----------------------------------------
# My Singly Linked List Unit Testing
# 2022-08-07
# ----------------------------------------
# Goal:
# Implement unit testing for singly linked list
# Desired functions:
# - size() - returns number of data elements in list
# - empty() - bool returns true if empty
# - value_at(index) - returns the value of the nth item (starting at 0 for first)
# - push_front(value) - adds an item to the front of the list
# - pop_front() - remove front item and return its value
# - push_back(value) - adds an item at the end
# - pop_back() - removes end item and returns its value
# - front() - get value of front item
# - back() - get value of end item
# - insert(index, value) - insert value at index, so current item at that index is pointed to by new item at index
# - erase(index) - removes node at given index
# - value_n_from_end(n) - returns the value of the node at nth position from the end of the list
# - reverse() - reverses the list
# - remove_value(value) - removes the first item in the list with this value

import my_singly_linked_list
import pytest

# size() - should return number of data elements in list
def test_s_list_size():
    test_s_list = my_singly_linked_list.my_s_list()
    assert test_s_list.size() == 0
    test_s_list.push_front(5)
    assert test_s_list.size() == 1
    for i in range(0, 10):
        test_s_list.push_front(i)
    assert test_s_list.size() == 11

# empty() - bool returns true if empty
def test_s_list_empty():
    test_s_list = my_singly_linked_list.my_s_list()
    assert test_s_list.empty() == True
    test_s_list.push_front(5)
    assert test_s_list.empty() == False

# value_at(index) - should return the value of the nth item (starting at 0 for first)
def test_s_list_value_at():
    test_s_list = my_singly_linked_list.my_s_list()
    test_s_list.push_front(5)
    test_s_list.push_front(10)
    assert test_s_list.value_at(0) == 10
    assert test_s_list.value_at(1) == 5
    with pytest.raises(Exception):
        assert test_s_list.value_at(-1)
        assert test_s_list.value_at(test_s_list.size())


# - push_front(value) - shoul add an item to the front of the list
def test_s_list_push_front():
    test_s_list = my_singly_linked_list.my_s_list()
    test_s_list.push_front(5)
    assert test_s_list.value_at(0) == 5

# - pop_front() - should remove front item and return its value
def test_s_list_pop_front():
    test_s_list = my_singly_linked_list.my_s_list()
    test_s_list.push_front(5)
    assert test_s_list.pop_front() == 5

# - push_back(value) - should add an item at the end
def test_s_listPushBack():
    test_s_list = my_singly_linked_list.my_s_list()
    for i in range(0, 5):
        test_s_list.push_front(i)
    test_s_list.push_back(13)
    assert test_s_list.value_at(test_s_list.size() - 1) == 13

# - pop_back() - should remove end item and returns its value
def test_s_listPopBack():
    test_s_list = my_singly_linked_list.my_s_list()
    test_s_list.push_front(5)
    test_s_list.push_back(13)
    assert test_s_list.pop_back() == 13

# - front() - should get value of front item
def test_s_listFront():
    test_s_list = my_singly_linked_list.my_s_list()
    test_s_list.push_front(5)
    assert test_s_list.front() == 5

# - back() - should get value of end item
def test_s_listBack():
    test_s_list = my_singly_linked_list.my_s_list()
    test_s_list.push_front(5)
    test_s_list.push_front(10)
    test_s_list.push_back(13)
    assert test_s_list.back() == 13

# - insert(index, value) - should insert value at index, so current item at that index is pointed to by new item at index
def test_s_listInsert():
    test_s_list = my_singly_linked_list.my_s_list()
    test_s_list.push_front(5)
    test_s_list.push_front(10)
    test_s_list.insert(1, 13)
    assert test_s_list.value_at(1) == 13
    with pytest.raises(Exception):
        assert test_s_list.insert(100)
    test_s_list = my_singly_linked_list.my_s_list()
    with pytest.raises(Exception):
        assert test_s_list.insert(2)

# - erase(index) - should remove node at given index
def test_s_list_erase():
    test_s_list = my_singly_linked_list.my_s_list()
    test_s_list.push_front(15)
    test_s_list.push_front(10)
    test_s_list.push_front(5)
    assert test_s_list.value_at(1) == 10
    test_s_list.erase(1)
    assert test_s_list.value_at(1) == 15

# - value_v_from_end(n) - should return the value of the node at nth position from the end of the list
def test_s_list_value_v_from_end():
    test_s_list = my_singly_linked_list.my_s_list()
    for i in range(5, 40, 5):
        test_s_list.push_front(i)
    assert test_s_list.value_n_from_end(2) == 15

# - reverse() - should reverse the list
def test_s_list_reverse():
    test_s_list = my_singly_linked_list.my_s_list()
    for i in range(5, 30, 5):
        test_s_list.push_front(i)
    assert test_s_list.value_at(3) == 10
    test_s_list.reverse()
    assert test_s_list.value_at(3) == 20

# - remove_value(value) - should remove the first item in the list with this value
def test_s_list_remove_value():
    test_s_list = my_singly_linked_list.my_s_list()
    for i in range(0, 25, 5):
        test_s_list.push_front(i)
    test_s_list.remove_value(15)
    assert test_s_list.value_at(1) == 10
    