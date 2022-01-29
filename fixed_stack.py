class Fixedstack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.item = [0] * capacity
        self.top_element = -1

    def push(self, element):
        """push new element in the stack"""
        assert self.capacity > self.top_element + 1, "stack overflow. Maximum capacity of stack exceeded (Max " + str(self.capacity) + " ) "
        self.item[self.top_element] = element
        self.top_element += 1


