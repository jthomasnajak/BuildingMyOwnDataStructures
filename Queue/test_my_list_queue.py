# # ----------------------------------------
# My List Queue Unit Testing
# 2022-08-20
# ----------------------------------------
# Goal:
# Implement a queue stored as an list
# desired functions:
# enqueue(Value) - adds item at end of available storage
# dequeue() - returns value and removes least recently added element
# empty() - returns true if queue is empty
# full() - returns true if queue is full

import my_list_queue

# should add item to end of queue
def test_my_list_queue_enqueue():
    test_queue = my_list_queue.my_list_queue()
    for i in range(0, 7):
        test_queue.enqueue(i)
    for i in range(0, 7):
        assert test_queue.dequeue() == i

# should remove least recently added element
def test_my_list_queue_dequeue():
    test_queue = my_list_queue.my_list_queue()
    for i in range(0, 7):
        test_queue.enqueue(i)
    assert test_queue.dequeue() == 0
    assert test_queue.dequeue() == 1
    test_queue.enqueue(10)
    assert test_queue.dequeue() == 2

# should return true if empty
def test_my_list_queue_empty():
    test_queue = my_list_queue.my_list_queue()
    assert test_queue.empty() == True
    test_queue.enqueue(1)
    assert test_queue.empty() == False