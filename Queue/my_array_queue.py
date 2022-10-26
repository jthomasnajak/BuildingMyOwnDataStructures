# ----------------------------------------
# My Array Queue
# 2022-08-17
# ----------------------------------------
# Goal:
# implement a queue stored as an array

class my_array_queue:

    current_array_size = 8
    internal_array = current_array_size * [None]
    enqueue_index = 0
    dequeue_index = 0

    def __init__(self):
        pass

    # adds item at end of available storage
    def enqueue(self, value):
        if (not self.full()):
            self.internal_array[self.enqueue_index] = value
            self.enqueue_index += 1
            if(self.enqueue_index == self.current_array_size):
                self.enqueue_index = 0
        else:
            raise Exception("cannot enqueue to full queue")

    # removes and returns least recently added element
    def dequeue(self):
        if (not self.empty()):
            return_value = self.internal_array[self.dequeue_index]
            self.dequeue_index += 1
            if (self.dequeue_index == self.current_array_size):
                self.dequeue_index = 0
            return return_value
        else:
            raise Exception("cannot dequeu from empty queue")

    # returns true if empty
    def empty(self):
        return (self.enqueue_index == self.dequeue_index)

    # returns true if full
    def full(self):
        return (self.enqueue_index == (self.dequeue_index - 1) \
            or ((self.enqueue_index == self.current_array_size - 1) and self.dequeue_index == 0))

    def output_as_string(self):
        output = "["
        for i in range(0, self.current_array_size - 1):
            output += str(self.internal_array[i]) + ", "
        output += str(self.internal_array[self.current_array_size - 1]) + "]"
        print(output)

my_test_queue = my_array_queue()