# ----------------------------------------
# My Array Unit Testing
# 2022-07-17
# ----------------------------------------
# Goals:
# - Gain experience writing and using unit tests
# - Test MyArray object class

import MyArray

# size() - number of items
def test_MyArraySize():
    TestArray = MyArray.MyIntArray(0)
    assert TestArray.size == 0
    TestArray = MyArray.MyIntArray(3)
    assert TestArray.size == 3

# capacity() - number of items it can hold
def test_MyArrayCapacity():
    TestArray = MyArray.MyIntArray(0)
    assert TestArray.capacity == 16
    TestArray = MyArray.MyIntArray(18)
    assert TestArray.capacity == 32

# is_empty()
def test_MyArrayisEmpty():
    TestArray = MyArray.MyIntArray(0)
    assert TestArray.isEmpty() == True
    TestArray = MyArray.MyIntArray(4)
    assert TestArray.isEmpty() == False

# at(index) - returns item at given index, blows up if index out of bounds
def test_MyArrayAt():
    TestArray = MyArray.MyIntArray(0)
    TestArray.push(5)
    assert TestArray.at(0) == 5

# push(item)
def test_MyArrayPush():
    TestArray = MyArray.MyIntArray(0)
    TestArray.push(5)
    assert TestArray.internalArray == [5, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

# insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
def test_MyArrayInsert():
    TestArray = MyArray.MyIntArray(0)
    for i in range(0, 4):
        TestArray.push(i)
    TestArray.insert(2, 10)
    assert TestArray.internalArray == [0, 1, 10, 2, 3, None, None, None, None, None, None, None, None, None, None, None]

# prepend(item) - can use insert above at index 0
def test_MyArrayPrepend():
    TestArray = MyArray.MyIntArray(0)
    TestArray.prepend(10)
    assert TestArray.at(0) == 10

# pop() - remove from end, return value
def test_MyArrayPop():
    TestArray = MyArray.MyIntArray(0)
    TestArray.push(5)
    assert TestArray.pop() == 5

# delete(index) - delete item at index, shifting all trailing elements left
def test_MyArrayDelete():
    TestArray = MyArray.MyIntArray(0)
    for i in range(0, 5):
        TestArray.push(i)
    TestArray.delete(2)
    assert TestArray.internalArray == [0, 1, 3, 4, 4, None, None, None, None, None, None, None, None, None, None, None]

# remove(item) - looks for value and removes index holding it (even if in multiple places)
def test_MyArrayRemove():
    TestArray = MyArray.MyIntArray(0)
    TestArray.push(5)
    TestArray.push(10)
    TestArray.push(5)
    TestArray.push(15)
    TestArray.remove(5)
    assert TestArray.size == 2
    assert TestArray.at(0) == 10
    assert TestArray.at(1) == 15


# find(item) - looks for value and returns first index with that value, -1 if not found
def test_MyArrayFind():
    TestArray = MyArray.MyIntArray(0)
    for i in range(0, 50, 5):
        TestArray.push(i)
    assert TestArray.find(15) == 3
    assert TestArray.find(100) == -1