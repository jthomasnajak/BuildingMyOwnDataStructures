# ----------------------------------------
# My Linked List
# 2022-07-11
# ----------------------------------------
# Goal:
# Implement a singly linked list

class LinkedList:
    """Implementation of a singly linked list. ....
    """
    
    class _ListNode:

        def __init__(self, value, next_node = None):
            self.value = value
            self.next = next_node

    def __init__(self) -> None:
        self.head = None
    
    # returns number of data elements in the list
    def size(self):
        if not self.head:
            return 0
        temp_size, temp_node = 0, self.head
        while temp_node:
            temp_size, temp_node = temp_size + 1, temp_node.next
        return temp_size
        
    # returns true if empty
    def empty(self):
        return self.head == None

    # returns the value of the nth item (starting at 0 for first)
    def value_at(self, index):
        if not self.head:
            raise ValueError("The list is empty. Cannot access index " + str(index))
        current_node = self.head
        for i in range(0, index):
            if (current_node.next != None):
                current_node = current_node.next
            else:
                raise IndexError(f"Index {index} is greater than list size: {i+1}")
        return current_node.value
        
    # adds an item to the front of the list
    def push_front(self, value):
        self.head = LinkedList._ListNode(value, self.head)

    # removes front item and returns its value
    def pop_front(self):
        if(self.head != None):
            return_value = self.head.value
            self.head = self.head.next
            return return_value
        else:
            raise Exception("list is currently empty")

    def push_back(self, value):
        if (self.head != None):
            current_node = self.head
            while(current_node.next != None):
                current_node = current_node.next
            current_node.next = LinkedList._ListNode(value)
        else:
            self.head = LinkedList._ListNode(value)

    def pop_back(self):
        if (self.head != None):
            current_node = self.head
            while(current_node.next.next != None):
                current_node = current_node.next
            return_value = current_node.next.value
            current_node.next = None
            return return_value
        else:
            raise Exception("list is currently Empty")

    # get value of front item
    def front(self):
        if (self.head != None):
            return self.head.value
        else:
            raise Exception("list is currently empty")
    
    # get value of end item
    def back(self):
        if (self.head != None):
            current_node = self.head
            while(current_node.next != None):
                current_node = current_node.next
            return current_node.value
        else:
            raise Exception("list is currently empty")

    # insert value at index, so current item at that index is pointed to by new item at index
    def insert(self, index, value):
        if (self.head != None):
            current_node = self.head
            for i in range(1, index):
                if(current_node.next != None):
                    current_node = current_node.next
                else:
                    raise Exception("reached end of list before reaching provided index")
            current_node.next = LinkedList._ListNode(value, current_node.next)
        else:
            raise Exception("list is currently empty")

    # removes node at given index
    def erase(self, index):
        if (self.head != None):
            current_node = self.head
            for i in range(1, index):
                if (current_node.next != None):
                    current_node = current_node.next
                else:
                    raise Exception("reached end of list before reaching provided index")
            current_node.next = current_node.next.next
        else:
            raise Exception("list is currently empty")

    # returns the value of the node at nth position from the end of the list
    def value_n_from_end(self, n):
        list_size = self.size()
        if(n >= list_size):
            raise Exception("provided n value is greater than length of list")
        elif (n < 0):
            raise Exception("provided n value cannot be less than zero")
        else:
            current_node = self.head
            for i in range(1, list_size - n):
                current_node = current_node.next
            return current_node.value

    # reverse the list
    def reverse(self):
        if (self.head != None):
            if (self.head.next != None):
                prev_node = None
                current_node = self.head
                next_node = self.head.next
                while(next_node != None):
                    current_node.next = prev_node
                    prev_node = current_node
                    current_node = next_node
                    next_node = next_node.next
                current_node.next = prev_node
                self.head = current_node
            else:
                raise Exception("cannot reverse list of length 1")
        else:
            raise Exception("list is empty")

    # removes the first item in the list with this value
    def remove_value(self, value):
        if (self.head != None):
            if (self.head.value == value):
                self.head = self.head.next
            else:
                current_node = self.head
                while(current_node.next.value != value and current_node.next.next != None):
                    current_node = current_node.next
                if (current_node.next.value == value):
                    current_node.next = current_node.next.next
                elif (current_node.next.next == None):
                    raise Exception("value not found within list")
        else: 
            raise Exception("cannot remove item from empty list")

    # output list as a string
    def output_list(self):
        if (self.head != None):
            current_node = self.head
            output = "head -> " + str(current_node.value) + " -> "
            while(current_node.next != None):
                current_node = current_node.next
                output += str(current_node.value) + " -> "
            output += "None"
            print(output)
        else:
            print("list is empty")