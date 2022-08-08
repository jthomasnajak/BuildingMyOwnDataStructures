# ----------------------------------------
# My Array
# 2022-07-11
# ----------------------------------------
# Goal:
# Implement a vector (mutable array with automatic resizing)
# > can allocate int array under the hood, just not use its features
# > start with 16, or if starting number is greater, use power of 2 - 16, 32, 64, 128

class MyIntArray:

    internalArray = [] # uses Array under the hood
    size = 0 # represents number of items
    capacity = 0 # represents number of items it can hold
    empty = True

    def __init__(self, length):
        self.size = length
        initialCapacity = 16
        while initialCapacity <= length:
            initialCapacity *= 2
        self.capacity = initialCapacity
        self.internalArray = [None] * self.capacity
        for i in range(0, self.size):
            self.internalArray[i] = 0
        if(self.size > 0):
            self.empty = False

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.capacity
    
    def isEmpty(self):
        return self.empty

    # returns item at specified index
    def at(self, index):
        if(index >= 0 and index < self.size):
            return self.internalArray[index]
        else:
            raise Exception("Provided Index is out of bounds")

    # appends given item to the end of the array
    def push(self, item):
        if(self.size == self.capacity):
            self.__resize(self.capacity * 2)
        self.internalArray[self.size] = item
        self.size += 1
        self.empty = False

    # inserts item at given index, shifts all trailing items right
    def insert(self, index, item):
        if (self.size == self.capacity):
            self.__resize(self.capacity * 2)
        for x in range(self.size, index - 1, -1):
            if (x > index):
                self.internalArray[x + 1] = self.internalArray[x]
            elif (x == index):
                self.internalArray[x + 1] = self.internalArray[x]
                self.internalArray[x] = item
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
            returnValue = self.internalArray[self.size]
            self.internalArray[self.size] = None
            if(self.size < (self.capacity / 4)):
                self.__resize(int(self.capacity / 2))
            return returnValue
        else:
            return None

    # deletes item at given index and shifts all trailing items left
    def delete(self, index):
        if(index > 0 and index < self.size):
            for x in range(index, self.size - 1):
                self.internalArray[x] = self.internalArray[x + 1]
            self.size -= 1

    # removes all instances of given item and shifts trailing items left
    def remove(self, item):
        NumberOfInstances = 0
        itemFound = False
        for x in range(1, self.size):
            if (self.internalArray[x - 1] == item):
                NumberOfInstances += 1
                itemFound = True
            if (itemFound):
                self.internalArray[x - NumberOfInstances] = self.internalArray[x]
        self.size -= NumberOfInstances

    # returns first index of given item or -1 if not found
    def find(self, item):
        for x in range(0, self.size):
            if (self.internalArray[x] == item):
                return x
        return -1

    # resizes the internal array
    def __resize(self, newCapacity):
        if(self.capacity != newCapacity):
            newArray = [None] * newCapacity
            if(newCapacity < self.capacity):
                newSize = 0
                for x in range(0, newCapacity):
                    newArray[x] = self.internalArray[x]
                    if(newArray[x] != None):
                        newSize += 1
                self.internalArray = newArray
                self.size = newSize
                self.capacity = newCapacity
            else:
                for x in range(0, self.size):
                    newArray[x] = self.internalArray[x]
                self.internalArray = newArray
                self.capacity = newCapacity
            
    # prints an output string of all elements
    def outputString(self):
        output = ""
        for x in range(0, self.size):
            output += (str(self.internalArray[x]) + ", ")
        print(output)