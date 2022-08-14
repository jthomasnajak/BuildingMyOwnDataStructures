# ----------------------------------------
# My Doubly Linked List with Tail Pointer and sentinel Node
# 2022-08-07
# ----------------------------------------
# Goal:
# Implement a doubly linked list with a tail pointer and a sentinel node

# Node Class
class MyDListNode:

    Value = None # contains node's value
    Next = None # points to next node
    Prev = None # points to previous node

    def __init__(Self, PassedValue, PassedNextNode = None, PassedPrevNode = None):

        Self.Value = PassedValue
        Self.Next = PassedNextNode
        Self.Prev = PassedPrevNode

# Linked List class
class MyDList:

    SentinelNode = MyDListNode(None)

    def __init__(Self):
        Self.SentinelNode.Next = Self.SentinelNode
        Self.SentinelNode.Prev = Self.SentinelNode

    # returns number of data elements in list
    def Size(Self):
        ReturnSize = 0
        CurrentNode = Self.SentinelNode.Next
        while (CurrentNode.Value != None):
            CurrentNode = CurrentNode.Next
            ReturnSize += 1
        return ReturnSize

    # bool returns true if empty
    def Empty(Self):
        return (Self.SentinelNode.Next.Value == None)

    # returns the value of the nth item (starting at 0 for first)
    def ValueAt(Self, Index):
        CurrentNode = Self.SentinelNode.Next
        for i in range(0, Index):
            if (CurrentNode.Value != None):
                CurrentNode = CurrentNode.Next
            else:
                raise Exception("provided index is greater than list length")
        return CurrentNode.Value

    # adds an item to the front of the list
    def PushFront(Self, Value):
        Self.SentinelNode.Next.Prev = MyDListNode(Value, Self.SentinelNode.Next, Self.SentinelNode)
        Self.SentinelNode.Next = Self.SentinelNode.Next.Prev

    # remove front item and return its value
    def PopFront(Self):
        ReturnValue = Self.SentinelNode.Next.Value
        Self.SentinelNode.Next = Self.SentinelNode.Next.Next
        Self.SentinelNode.Next.Prev = Self.SentinelNode
        return ReturnValue

    # adds an item at the end
    def PushBack(Self, Value):
        Self.SentinelNode.Prev.Next = MyDListNode(Value, Self.SentinelNode, Self.SentinelNode.Prev)
        Self.SentinelNode.Prev = Self.SentinelNode.Prev.Next

    # removes end item and returns its value
    def PopBack(Self):
        ReturnValue = Self.SentinelNode.Prev.Value
        Self.SentinelNode.Prev = Self.SentinelNode.Prev.Prev
        Self.SentinelNode.Prev.Next = Self.SentinelNode
        return ReturnValue

    # get value of front item
    def Front(Self):
        return Self.SentinelNode.Next.Value

    # get value of end item
    def Back(Self):
        return Self.SentinelNode.Prev.Value

    # insert value at index, so current item at that index is pointed to by new item at index
    def Insert(Self, Index, Value):
        CurrentNode = Self.SentinelNode.Next
        for i in range(1, Index):
            if CurrentNode.Value == None:
                raise Exception("reached end of list before provided index")
            else:
                CurrentNode = CurrentNode.Next
        CurrentNode.Next = MyDListNode(Value, CurrentNode.Next, CurrentNode)
        CurrentNode.Next.Next.Prev = CurrentNode.Next

    # removes node at given index
    def Erase(Self, Index):
        CurrentNode = Self.SentinelNode.Next
        for i in range(1, Index):
            if (CurrentNode.Value == None):
                raise Exception("reached end of list before provided index")
            else:
                CurrentNode = CurrentNode.Next
        CurrentNode.Next = CurrentNode.Next.Next
        CurrentNode.Next.Prev = CurrentNode

    # returns the value of the node at nth position from the end of the list
    def ValueNFromEnd(Self, N):
        CurrentNode = Self.SentinelNode.Prev
        for i in range(0, N):
            if (CurrentNode.Value != None):
                CurrentNode = CurrentNode.Prev
            else:
                raise Exception("provided index is greater than list length")
        return CurrentNode.Value

    # reverses the list
    def Reverse(Self):
        CurrentNode = Self.SentinelNode
        TempNode = CurrentNode.Next
        CurrentNode.Next = CurrentNode.Prev
        CurrentNode.Prev = TempNode
        CurrentNode = TempNode
        TempNode = TempNode.Next
        while (CurrentNode.Value != None):
            CurrentNode.Next = CurrentNode.Prev
            CurrentNode.Prev = TempNode
            CurrentNode = TempNode
            TempNode = TempNode.Next

    # removes the first item in the list with this value
    def RemoveValue(Self, Value):
        CurrentNode = Self.SentinelNode
        while(CurrentNode.Next.Value != Value and CurrentNode.Next.Value != None):
            CurrentNode = CurrentNode.Next
        if (CurrentNode.Next.Value == Value):
            CurrentNode.Next = CurrentNode.Next.Next
            CurrentNode.Next.Prev = CurrentNode
        else:
            raise Exception("provided value not found within list")

    # outputs the list as a string
    def OutputList(Self):
        OutputString = "Sentinel <-> "
        CurrentNode = Self.SentinelNode.Next
        while(CurrentNode.Value != None):
            OutputString += (str(CurrentNode.Value) + " <-> ")
            CurrentNode = CurrentNode.Next
        OutputString += "Sentinel"
        print(OutputString)