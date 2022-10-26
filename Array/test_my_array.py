# ----------------------------------------
# My Array Unit Testing
# 2022-07-17
# ----------------------------------------
# Goals:
# - Gain experience writing and using unit tests
# - Test my_array object class

import my_array

# size() - number of items
def test_my_array_size():
    test_array = my_array.my_int_array(0)
    assert test_array.get_size() == 0
    test_array = my_array.my_int_array(3)
    assert test_array.get_size() == 3

# capacity() - number of items it can hold
def test_my_arrayCapacity():
    test_array = my_array.my_int_array(0)
    assert test_array.get_capacity() == 16
    test_array = my_array.my_int_array(18)
    assert test_array.get_capacity() == 32

# is_empty()
def test_my_arrayisEmpty():
    test_array = my_array.my_int_array(0)
    assert test_array.is_empty() == True
    test_array = my_array.my_int_array(4)
    assert test_array.is_empty() == False

# at(index) - returns item at given index, blows up if index out of bounds
def test_my_arrayAt():
    test_array = my_array.my_int_array(0)
    test_array.push(5)
    assert test_array.at(0) == 5

# push(item)
def test_my_arrayPush():
    test_array = my_array.my_int_array(0)
    test_array.push(5)
    assert test_array.internal_array == [5, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

# insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
def test_my_arrayInsert():
    test_array = my_array.my_int_array(0)
    for i in range(0, 4):
        test_array.push(i)
    test_array.insert(2, 10)
    assert test_array.internal_array == [0, 1, 10, 2, 3, None, None, None, None, None, None, None, None, None, None, None]

# prepend(item) - can use insert above at index 0
def test_my_arrayPrepend():
    test_array = my_array.my_int_array(0)
    test_array.prepend(10)
    assert test_array.at(0) == 10

# pop() - remove from end, return value
def test_my_arrayPop():
    test_array = my_array.my_int_array(0)
    test_array.push(5)
    assert test_array.pop() == 5

# delete(index) - delete item at index, shifting all trailing elements left
def test_my_arrayDelete():
    test_array = my_array.my_int_array(0)
    for i in range(0, 5):
        test_array.push(i)
    test_array.delete(2)
    assert test_array.internal_array == [0, 1, 3, 4, 4, None, None, None, None, None, None, None, None, None, None, None]

# remove(item) - looks for value and removes index holding it (even if in multiple places)
def test_my_arrayRemove():
    test_array = my_array.my_int_array(0)
    test_array.push(5)
    test_array.push(10)
    test_array.push(5)
    test_array.push(15)
    test_array.remove(5)
    assert test_array.size == 2
    assert test_array.at(0) == 10
    assert test_array.at(1) == 15


# find(item) - looks for value and returns first index with that value, -1 if not found
def test_my_arrayFind():
    test_array = my_array.my_int_array(0)
    for i in range(0, 50, 5):
        test_array.push(i)
    assert test_array.find(15) == 3
    assert test_array.find(100) == -1