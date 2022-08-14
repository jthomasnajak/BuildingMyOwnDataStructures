# ----------------------------------------
# My Doubly Linked List Unit Testing
# 2022-08-13
# ----------------------------------------
# Goal:
# Implement unit testing for doubly linked list
# Desired functions:
# - Size() - returns number of data elements in list
# - Empty() - bool returns true if empty
# - ValueAt(index) - returns the value of the nth item (starting at 0 for first)
# - PushFront(value) - adds an item to the front of the list
# - PopFront() - remove front item and return its value
# - PushBack(value) - adds an item at the end
# - PopBack() - removes end item and returns its value
# - Front() - get value of front item
# - Back() - get value of end item
# - Insert(index, value) - insert value at index, so current item at that index is pointed to by new item at index
# - Erase(index) - removes node at given index
# - ValueNFromEnd(n) - returns the value of the node at nth position from the end of the list
# - Reverse() - reverses the list
# - RemoveValue(value) - removes the first item in the list with this value

import MyDoublyLinkedList
#import pytest

# Size() - should return number of data elements in list
def test_DListSize():
    TestDList = MyDoublyLinkedList.MyDList()
    assert TestDList.Size() == 0
    TestDList.PushFront(5)
    assert TestDList.Size() == 1
    for i in range(0, 10):
        TestDList.PushFront(i)
    assert TestDList.Size() == 11

# Empty() - bool returns true if empty
def test_DListEmpty():
    TestDList = MyDoublyLinkedList.MyDList()
    assert TestDList.Empty() == True
    TestDList.PushFront(5)
    assert TestDList.Empty() == False

# ValueAt(index) - should return the value of the nth item (starting at 0 for first)
def test_DListValueAt():
    TestDList = MyDoublyLinkedList.MyDList()
    TestDList.PushFront(5)
    TestDList.PushFront(10)
    assert TestDList.ValueAt(0) == 10
    assert TestDList.ValueAt(1) == 5
    #with pytest.raises(Exception):
    #    assert TestDList.ValueAt(-1)
    #    assert TestDList.ValueAt(TestDList.Size())


# - PushFront(value) - shoul add an item to the front of the list
def test_DListPushFront():
    TestDList = MyDoublyLinkedList.MyDList()
    TestDList.PushFront(5)
    assert TestDList.ValueAt(0) == 5

# - PopFront() - should remove front item and return its value
def test_DListPopFront():
    TestDList = MyDoublyLinkedList.MyDList()
    TestDList.PushFront(5)
    assert TestDList.PopFront() == 5

# - PushBack(value) - should add an item at the end
def test_DListPushBack():
    TestDList = MyDoublyLinkedList.MyDList()
    for i in range(0, 5):
        TestDList.PushFront(i)
    TestDList.PushBack(13)
    assert TestDList.ValueAt(TestDList.Size() - 1) == 13

# - PopBack() - should remove end item and returns its value
def test_DListPopBack():
    TestDList = MyDoublyLinkedList.MyDList()
    TestDList.PushFront(5)
    TestDList.PushBack(13)
    assert TestDList.PopBack() == 13

# - Front() - should get value of front item
def test_DListFront():
    TestDList = MyDoublyLinkedList.MyDList()
    TestDList.PushFront(5)
    assert TestDList.Front() == 5

# - Back() - should get value of end item
def test_DListBack():
    TestDList = MyDoublyLinkedList.MyDList()
    TestDList.PushFront(5)
    TestDList.PushFront(10)
    TestDList.PushBack(13)
    assert TestDList.Back() == 13

# - Insert(index, value) - should insert value at index, so current item at that index is pointed to by new item at index
def test_DListInsert():
    TestDList = MyDoublyLinkedList.MyDList()
    TestDList.PushFront(5)
    TestDList.PushFront(10)
    TestDList.Insert(1, 13)
    assert TestDList.ValueAt(1) == 13
    #with pytest.raises(Exception):
    #    assert TestDList.Insert(100)
    TestDList = MyDoublyLinkedList.MyDList()
    #with pytest.raises(Exception):
    #    assert TestDList.Insert(2)

# - Erase(index) - should remove node at given index
def test_DListErase():
    TestDList = MyDoublyLinkedList.MyDList()
    TestDList.PushFront(15)
    TestDList.PushFront(10)
    TestDList.PushFront(5)
    assert TestDList.ValueAt(1) == 10
    TestDList.Erase(1)
    assert TestDList.ValueAt(1) == 15

# - ValueNFromEnd(n) - should return the value of the node at nth position from the end of the list
def test_DListValueNFromEnd():
    TestDList = MyDoublyLinkedList.MyDList()
    for i in range(5, 40, 5):
        TestDList.PushFront(i)
    assert TestDList.ValueNFromEnd(2) == 15

# - Reverse() - should reverse the list
def test_DListReverse():
    TestDList = MyDoublyLinkedList.MyDList()
    for i in range(5, 30, 5):
        TestDList.PushFront(i)
    assert TestDList.ValueAt(3) == 10
    TestDList.Reverse()
    assert TestDList.ValueAt(3) == 20

# - RemoveValue(value) - should remove the first item in the list with this value
def test_DListRemoveValue():
    TestDList = MyDoublyLinkedList.MyDList()
    for i in range(0, 25, 5):
        TestDList.PushFront(i)
    TestDList.RemoveValue(15)
    assert TestDList.ValueAt(1) == 10
    
