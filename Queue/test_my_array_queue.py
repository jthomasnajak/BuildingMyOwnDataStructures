# # ----------------------------------------
# My Array Queue Unit Testing
# 2022-08-17
# ----------------------------------------
# Goal:
# Implement a queue stored as an array
# desired functions:
# enqueue(Value) - adds item at end of available storage
# dequeue() - returns value and removes least recently added element
# empty() - returns true if queue is empty
# full() - returns true if queue is full

import my_array_queue

# should add item to end of queue
def test_my_array_queue_enqueue():
    test_queue = my_array_queue.my_array_queue()
    for i in range(0, test_queue.current_array_size - 1):
        test_queue.enqueue(i)
    assert test_queue.internal_array == [0, 1, 2, 3, 4, 5, 6, None]

# should remove least recently added element
def test_my_array_queue_dequeue():
    test_queue = my_array_queue.my_array_queue()
    for i in range(0, 7):
        test_queue.enqueue(i)
    assert test_queue.dequeue() == 0
    assert test_queue.dequeue() == 1
    test_queue.enqueue(10)
    assert test_queue.dequeue() == 2

# should return true if empty
def test_my_array_queue_empty():
    test_queue = my_array_queue.my_array_queue()
    assert test_queue.empty() == True
    test_queue.enqueue(1)
    assert test_queue.empty() == False

# should return true if full
def test_my_array_queue_full():
    test_queue = my_array_queue.my_array_queue()
    for i in range(0, test_queue.current_array_size - 2):
        test_queue.enqueue(i)
        assert test_queue.full() == False
    test_queue.enqueue(10)
    assert test_queue.full() == True
    