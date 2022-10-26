# ----------------------------------------
# My Array Stack
# 2022-08-14
# ----------------------------------------
# Goal:
# Implement a Stack stored as an array


class my_array_stack:

    internal_array = 16 * [None]
    current_top_index = 0

    def __init__(self):
        pass

    # pushes value to top of stack
    def push(self, value):
        self.internal_array[self.current_top_index] = value
        self.current_top_index += 1

    # returns value at top of stack
    def top(self):
        return self.internal_array[self.current_top_index - 1]

    # removes and returns value at top of stack
    def pop(self):
        return_value = self.internal_array[self.current_top_index - 1]
        self.internal_array[self.current_top_index - 1] = None
        self.current_top_index -= 1
        return return_value

    # returns true if stack is empty
    def empty(self):
        return (self.current_top_index == 0)

    # outputs stack as string
    def output_as_string(self):
        output = ""
        for i in range(1, self.current_top_index + 1):
            output += str(self.internal_array[self.current_top_index - i]) + ", "
        print(output)