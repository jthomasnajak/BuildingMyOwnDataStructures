# ----------------------------------------
# My Singly Linked List Unit Testing
# 2022-08-07
# ----------------------------------------
# Goal:
# Implement unit testing for singly linked list
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

import MySinglyLinkedList
#import pytest

# Size() - should return number of data elements in list
def test_SListSize():
    TestSList = MySinglyLinkedList.MySList()
    assert TestSList.Size() == 0
    TestSList.PushFront(5)
    assert TestSList.Size() == 1
    for i in range(0, 10):
        TestSList.PushFront(i)
    assert TestSList.Size() == 11

# Empty() - bool returns true if empty
def test_SListEmpty():
    TestSList = MySinglyLinkedList.MySList()
    assert TestSList.Empty() == True
    TestSList.PushFront(5)
    assert TestSList.Empty() == False

# ValueAt(index) - should return the value of the nth item (starting at 0 for first)
def test_SListValueAt():
    TestSList = MySinglyLinkedList.MySList()
    TestSList.PushFront(5)
    TestSList.PushFront(10)
    assert TestSList.ValueAt(0) == 10
    assert TestSList.ValueAt(1) == 5
    #with pytest.raises(Exception):
    #    assert TestSList.ValueAt(-1)
    #    assert TestSList.ValueAt(TestSList.Size())


# - PushFront(value) - shoul add an item to the front of the list
def test_SListPushFront():
    TestSList = MySinglyLinkedList.MySList()
    TestSList.PushFront(5)
    assert TestSList.ValueAt(0) == 5

# - PopFront() - should remove front item and return its value
def test_SListPopFront():
    TestSList = MySinglyLinkedList.MySList()
    TestSList.PushFront(5)
    assert TestSList.PopFront() == 5

# - PushBack(value) - should add an item at the end
def test_SListPushBack():
    TestSList = MySinglyLinkedList.MySList()
    for i in range(0, 5):
        TestSList.PushFront(i)
    TestSList.PushBack(13)
    assert TestSList.ValueAt(TestSList.Size() - 1) == 13

# - PopBack() - should remove end item and returns its value
def test_SListPopBack():
    TestSList = MySinglyLinkedList.MySList()
    TestSList.PushFront(5)
    TestSList.PushBack(13)
    assert TestSList.PopBack() == 13

# - Front() - should get value of front item
def test_SListFront():
    TestSList = MySinglyLinkedList.MySList()
    TestSList.PushFront(5)
    assert TestSList.Front() == 5

# - Back() - should get value of end item
def test_SListBack():
    TestSList = MySinglyLinkedList.MySList()
    TestSList.PushFront(5)
    TestSList.PushFront(10)
    TestSList.PushBack(13)
    assert TestSList.Back() == 13

# - Insert(index, value) - should insert value at index, so current item at that index is pointed to by new item at index
def test_SListInsert():
    TestSList = MySinglyLinkedList.MySList()
    TestSList.PushFront(5)
    TestSList.PushFront(10)
    TestSList.Insert(1, 13)
    assert TestSList.ValueAt(1) == 13
    #with pytest.raises(Exception):
    #    assert TestSList.Insert(100)
    TestSList = MySinglyLinkedList.MySList()
    #with pytest.raises(Exception):
    #    assert TestSList.Insert(2)

# - Erase(index) - should remove node at given index
def test_SListErase():
    TestSList = MySinglyLinkedList.MySList()
    TestSList.PushFront(15)
    TestSList.PushFront(10)
    TestSList.PushFront(5)
    assert TestSList.ValueAt(1) == 10
    TestSList.Erase(1)
    assert TestSList.ValueAt(1) == 15

# - ValueNFromEnd(n) - should return the value of the node at nth position from the end of the list
def test_SListValueNFromEnd():
    TestSList = MySinglyLinkedList.MySList()
    for i in range(5, 40, 5):
        TestSList.PushFront(i)
    assert TestSList.ValueNFromEnd(2) == 15

# - Reverse() - should reverse the list
def test_SListReverse():
    TestSList = MySinglyLinkedList.MySList()
    for i in range(5, 30, 5):
        TestSList.PushFront(i)
    assert TestSList.ValueAt(3) == 10
    TestSList.Reverse()
    assert TestSList.ValueAt(3) == 20

# - RemoveValue(value) - should remove the first item in the list with this value
def test_SListRemoveValue():
    TestSList = MySinglyLinkedList.MySList()
    for i in range(0, 25, 5):
        TestSList.PushFront(i)
    TestSList.RemoveValue(15)
    assert TestSList.ValueAt(1) == 10
    
