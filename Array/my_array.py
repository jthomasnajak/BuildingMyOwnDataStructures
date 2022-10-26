# ----------------------------------------
# My Array
# 2022-07-11
# ----------------------------------------
# Goal:
# Implement a vector (mutable array with automatic resizing)
# > can allocate int array under the hood, just not use its features
# > start with 16, or if starting number is greater, use power of 2 - 16, 32, 64, 128

class my_int_array:

    internal_array = [] # uses array under the hood
    size = 0 # represents number of items
    capacity = 0 # represents number of items it can hold
    empty = True

    def __init__(self, length):
        self.size = length
        initial_capacity = 16
        while initial_capacity <= length:
            initial_capacity *= 2
        self.capacity = initial_capacity
        self.internal_array = [None] * self.capacity
        for i in range(0, self.size):
            self.internal_array[i] = 0
        if(self.size > 0):
            self.empty = False

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity
    
    def is_empty(self):
        return self.empty

    # returns item at specified index
    def at(self, index):
        if(index >= 0 and index < self.size):
            return self.internal_array[index]
        else:
            raise Exception("provided index is out of bounds")

    # appends given item to the end of the array
    def push(self, item):
        if(self.size == self.capacity):
            self.__reSize(self.capacity * 2)
        self.internal_array[self.size] = item
        self.size += 1
        self.empty = False

    # inserts item at given index, shifts all trailing items right
    def insert(self, index, item):
        if (self.size == self.capacity):
            self.__reSize(self.capacity * 2)
        for x in range(self.size, index - 1, -1):
            if (x > index):
                self.internal_array[x + 1] = self.internal_array[x]
            elif (x == index):
                self.internal_array[x + 1] = self.internal_array[x]
                self.internal_array[x] = item
        self.size += 1

    # inserts item at the initial position
    def prepend(self, item):
        self.insert(0, item)

    # removes and returns end item
    def pop(self):
        if(self.size > 0):
            self.size -= 1
            if(self.size == 0):
                self.empty = True
            return_value = self.internal_array[self.size]
            self.internal_array[self.size] = None
            if(self.size < (self.capacity / 4)):
                self.__reSize(int(self.capacity / 2))
            return return_value
        else:
            return None

    # deletes item at given index and shifts all trailing items left
    def delete(self, index):
        if(index > 0 and index < self.size):
            for x in range(index, self.size - 1):
                self.internal_array[x] = self.internal_array[x + 1]
            self.size -= 1

    # removes all instances of given item and shifts trailing items left
    def remove(self, item):
        number_of_instances = 0
        item_found = False
        for x in range(1, self.size):
            if (self.internal_array[x - 1] == item):
                number_of_instances += 1
                item_found = True
            if (item_found):
                self.internal_array[x - number_of_instances] = self.internal_array[x]
        self.size -= number_of_instances

    # returns first index of given item or -1 if not found
    def find(self, item):
        for x in range(0, self.size):
            if (self.internal_array[x] == item):
                return x
        return -1

    # ReSizes the internal array
    def __reSize(self, new_capacity):
        if(self.capacity != new_capacity):
            new_array = [None] * new_capacity
            if(new_capacity < self.capacity):
                new_size = 0
                for x in range(0, new_capacity):
                    new_array[x] = self.internal_array[x]
                    if(new_array[x] != None):
                        new_size += 1
                self.internal_array = new_array
                self.size = new_size
                self.Capacity = new_capacity
            else:
                for x in range(0, self.Size):
                    new_array[x] = self.internal_array[x]
                self.internal_array = new_array
                self.capacity = new_capacity
            
    # prints an output string of all elements
    def output_as_string(self):
        output = ""
        for x in range(0, self.size):
            output += (str(self.internal_array[x]) + ", ")
        print(output)