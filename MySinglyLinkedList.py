# ----------------------------------------
# My Linked List
# 2022-07-11
# ----------------------------------------
# Goal:
# Implement a singly linked list

# Node Class to build each node of the Linked List
class MySListNode:

    Value = None # contains node's value
    Next = None # pointer to next node

    def __init__(Self, PassedValue, PassedNextNode = None):

        Self.Value = PassedValue
        Self.Next = PassedNextNode


# Linked List class
class MySList:

    Head = None # head pointer

    # returns number of data elements in the list
    def Size(Self):
        if(Self.Head != None):
            CurrentNode = Self.Head
            ListSize = 1
            while(CurrentNode.Next != None):
                ListSize += 1
                CurrentNode = CurrentNode.Next
            return ListSize
        else:
            return 0

    # returns true if empty
    def Empty(Self):
        return (Self.Head == None)

    # returns the value of the nth item (starting at 0 for first)
    def ValueAt(Self, Index):
        if (Self.Head != None):
            CurrentNode = Self.Head
            for i in range(0, Index):
                if (CurrentNode.Next != None):
                    CurrentNode = CurrentNode.Next
                else:
                    raise Exception("provided index is greater than list size")
            return CurrentNode.Value
        else:
            raise Exception("list is currently empty")

    # adds an item to the front of the list
    def PushFront(Self, Value):
        Self.Head = MySListNode(Value, Self.Head)

    # removes front item and returns its value
    def PopFront(Self):
        if(Self.Head != None):
            ReturnValue = Self.Head.Value
            Self.Head = Self.Head.Next
            return ReturnValue
        else:
            raise Exception("list is currently empty")

    def PushBack(Self, Value):
        if (Self.Head != None):
            CurrentNode = Self.Head
            while(CurrentNode.Next != None):
                CurrentNode = CurrentNode.Next
            CurrentNode.Next = MySListNode(Value)
        else:
            Self.Head = MySListNode(Value)

    def PopBack(Self):
        if (Self.Head != None):
            CurrentNode = Self.Head
            while(CurrentNode.Next.Next != None):
                CurrentNode = CurrentNode.Next
            ReturnValue = CurrentNode.Next.Value
            CurrentNode.Next = None
            return ReturnValue
        else:
            raise Exception("list is currently Empty")

    # get value of front item
    def Front(Self):
        if (Self.Head != None):
            return Self.Head.Value
        else:
            raise Exception("list is currently empty")
    
    # get value of end item
    def Back(Self):
        if (Self.Head != None):
            CurrentNode = Self.Head
            while(CurrentNode.Next != None):
                CurrentNode = CurrentNode.Next
            return CurrentNode.Value
        else:
            raise Exception("list is currently empty")

    # insert value at index, so current item at that index is pointed to by new item at index
    def Insert(Self, Index, Value):
        if (Self.Head != None):
            CurrentNode = Self.Head
            for i in range(1, Index):
                if(CurrentNode.Next != None):
                    CurrentNode = CurrentNode.Next
                else:
                    raise Exception("reached end of list before reaching provided index")
            CurrentNode.Next = MySListNode(Value, CurrentNode.Next)
        else:
            raise Exception("list is currently empty")

    # removes node at given index
    def Erase(Self, Index):
        if (Self.Head != None):
            CurrentNode = Self.Head
            for i in range(1, Index):
                if (CurrentNode.Next != None):
                    CurrentNode = CurrentNode.Next
                else:
                    raise Exception("reached end of list before reaching provided index")
            CurrentNode.Next = CurrentNode.Next.Next
        else:
            raise Exception("list is currently empty")

    # returns the value of the node at nth position from the end of the list
    def ValueNFromEnd(Self, N):
        ListSize = Self.Size()
        if(N >= ListSize):
            raise Exception("provided n value is greater than length of list")
        elif (N < 0):
            raise Exception("provided n value cannot be less than zero")
        else:
            CurrentNode = Self.Head
            for i in range(1, ListSize - N):
                CurrentNode = CurrentNode.Next
            return CurrentNode.Value

    # reverse the list
    def Reverse(Self):
        if (Self.Head != None):
            if (Self.Head.Next != None):
                PrevNode = None
                CurrentNode = Self.Head
                NextNode = Self.Head.Next
                while(NextNode != None):
                    CurrentNode.Next = PrevNode
                    PrevNode = CurrentNode
                    CurrentNode = NextNode
                    NextNode = NextNode.Next
                CurrentNode.Next = PrevNode
                Self.Head = CurrentNode
            else:
                raise Exception("cannot reverse list of length 1")
        else:
            raise Exception("list is empty")

    # removes the first item in the list with this value
    def RemoveValue(Self, Value):
        if (Self.Head != None):
            if (Self.Head.Value == Value):
                Self.Head = Self.Head.Next
            else:
                CurrentNode = Self.Head
                while(CurrentNode.Next.Value != Value and CurrentNode.Next.Next != None):
                    CurrentNode = CurrentNode.Next
                if (CurrentNode.Next.Value == Value):
                    CurrentNode.Next = CurrentNode.Next.Next
                elif (CurrentNode.Next.Next == None):
                    raise Exception("value not found within list")
        else: 
            raise Exception("cannot remove item from empty list")

    # output list as a string
    def OutputList(Self):
        if (Self.Head != None):
            CurrentNode = Self.Head
            OutputString = "Head -> " + str(CurrentNode.Value) + " -> "
            while(CurrentNode.Next != None):
                CurrentNode = CurrentNode.Next
                OutputString += str(CurrentNode.Value) + " -> "
            OutputString += "None"
            print(OutputString)
        else:
            print("list is empty")



TestSList = MySList()
for i in range(5, 40, 5):
    TestSList.PushFront(i)
TestSList.OutputList()
TestSList.PushBack(13)
TestSList.OutputList()