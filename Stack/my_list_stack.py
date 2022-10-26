# ----------------------------------------
# My List Stack
# 2022-08-17
# ----------------------------------------
# Goal:
# Implement a stack stored as a singly linked list

from cgi import test


class my_list_stack_node:

    value = None
    next = None

    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class my_list_stack:

    head = None

    def __init__(self):
        pass

    # pushes value to top of stack
    def push(self, value):
        self.head = my_list_stack_node(value, self.head)

    # returns value at top of stack
    def top(self):
        return self.head.value

    # removes and returns value at top of stack
    def pop(self):
        return_value = self.head.value
        self.head = self.head.next
        return return_value

    # returns true if stack is emtpy
    def empty(self):
        return (self.head == None)

    # outputs stack as string
    def output_as_string(self):
        output = "head -> "
        current_node = self.head
        while (current_node != None):
            output += str(current_node.value) + " -> "
            current_node = current_node.next
        output += "None"
        print(output)
