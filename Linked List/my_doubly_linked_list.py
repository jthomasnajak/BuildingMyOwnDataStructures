# ----------------------------------------
# My Doubly Linked List with Tail Pointer and sentinel node
# 2022-08-07
# ----------------------------------------
# Goal:
# Implement a doubly linked list with a tail pointer and a sentinel node

# node class
from doctest import OutputChecker


class my_d_list_node:

    value = None # contains node's value
    next = None # points to next node
    prev = None # points to previous node

    def __init__(self, passed_value, passed_next_node = None, passed_prev_node = None):

        self.value = passed_value
        self.next = passed_next_node
        self.prev = passed_prev_node

# Linked List class
class my_d_list:

    sentinel_node = my_d_list_node(None)

    def __init__(self):
        self.sentinel_node.next = self.sentinel_node
        self.sentinel_node.prev = self.sentinel_node

    # returns number of data elements in list
    def size(self):
        return_size = 0
        current_node = self.sentinel_node.next
        while (current_node.value != None):
            current_node = current_node.next
            return_size += 1
        return return_size

    # bool returns true if empty
    def empty(self):
        return (self.sentinel_node.next.value == None)

    # returns the value of the nth item (starting at 0 for first)
    def value_at(self, Index):
        current_node = self.sentinel_node.next
        for i in range(0, Index):
            if (current_node.value != None):
                current_node = current_node.next
            else:
                raise Exception("provided index is greater than list length")
        return current_node.value

    # adds an item to the front of the list
    def push_front(self, value):
        self.sentinel_node.next.prev = my_d_list_node(value, self.sentinel_node.next, self.sentinel_node)
        self.sentinel_node.next = self.sentinel_node.next.prev

    # remove front item and return its value
    def pop_front(self):
        return_value = self.sentinel_node.next.value
        self.sentinel_node.next = self.sentinel_node.next.next
        self.sentinel_node.next.prev = self.sentinel_node
        return return_value

    # adds an item at the end
    def push_back(self, value):
        self.sentinel_node.prev.next = my_d_list_node(value, self.sentinel_node, self.sentinel_node.prev)
        self.sentinel_node.prev = self.sentinel_node.prev.next

    # removes end item and returns its value
    def pop_back(self):
        return_value = self.sentinel_node.prev.value
        self.sentinel_node.prev = self.sentinel_node.prev.prev
        self.sentinel_node.prev.next = self.sentinel_node
        return return_value

    # get value of front item
    def front(self):
        return self.sentinel_node.next.value

    # get value of end item
    def back(self):
        return self.sentinel_node.prev.value

    # insert value at index, so current item at that index is pointed to by new item at index
    def insert(self, index, value):
        current_node = self.sentinel_node.next
        for i in range(1, index):
            if current_node.value == None:
                raise Exception("reached end of list before provided index")
            else:
                current_node = current_node.next
        current_node.next = my_d_list_node(value, current_node.next, current_node)
        current_node.next.next.prev = current_node.next

    # removes node at given index
    def erase(self, index):
        current_node = self.sentinel_node.next
        for i in range(1, index):
            if (current_node.value == None):
                raise Exception("reached end of list before provided index")
            else:
                current_node = current_node.next
        current_node.next = current_node.next.next
        current_node.next.prev = current_node

    # returns the value of the node at nth position from the end of the list
    def value_n_from_end(self, n):
        current_node = self.sentinel_node.prev
        for i in range(0, n):
            if (current_node.value != None):
                current_node = current_node.prev
            else:
                raise Exception("provided index is greater than list length")
        return current_node.value

    # reverses the list
    def reverse(self):
        current_node = self.sentinel_node
        temp_node = current_node.next
        current_node.next = current_node.prev
        current_node.prev = temp_node
        current_node = temp_node
        temp_node = temp_node.next
        while (current_node.value != None):
            current_node.next = current_node.prev
            current_node.prev = temp_node
            current_node = temp_node
            temp_node = temp_node.next

    # removes the first item in the list with this value
    def remove_value(self, value):
        current_node = self.sentinel_node
        while(current_node.next.value != value and current_node.next.value != None):
            current_node = current_node.next
        if (current_node.next.value == value):
            current_node.next = current_node.next.next
            current_node.next.prev = current_node
        else:
            raise Exception("provided value not found within list")

    # outputs the list as a string
    def output_as_string(self):
        output = "sentinel <-> "
        current_node = self.sentinel_node.next
        while(current_node.value != None):
            output += (str(current_node.value) + " <-> ")
            current_node = current_node.next
        output += "sentinel"
        print(output)