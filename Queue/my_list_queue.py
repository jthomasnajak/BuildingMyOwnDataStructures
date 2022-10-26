# ----------------------------------------
# My List Queue
# 2022-08-20
# ----------------------------------------
# Goal:
# implement a queue stored as a singly linked list with tail pointer

class my_list_node:

    value = None 
    next = None

    def __init__(self, passed_value, passed_next_node = None):

        self.value = passed_value
        self.next = passed_next_node

class my_list_queue:

    head = None
    tail = None

    # adds item at end of queue
    def enqueue(self, value):
        if(self.empty()):
            self.head = my_list_node(value)
            self.tail = self.head
        else:
            self.tail.next = my_list_node(value)
            self.tail = self.tail.next

    # removes and returns least recently added item
    def dequeue(self):
        if (not self.empty()):
            return_value = self.head.value
            self.head = self.head.next
            return return_value
        else:
            raise Exception("cannot dequeue from empty list")


    # returns true if empty
    def empty(self):
        return (self.head == None)

    def output_as_string(self):
        current_node = self.head
        if (current_node != None):
            output = "[" + str(current_node.value)
            while (current_node.next != None):
                current_node = current_node.next
                output += ", " + str(current_node.value)
            output += "]"
        else:
            output = "queue is empty"
        print(output)

        