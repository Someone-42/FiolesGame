class Fixedstack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.item = [0] * capacity
        self.top_element = -1

    def push(self, element):
        """push new element in the stack"""
        assert self.capacity > self.top_element + 1, "stack overflow. Maximum capacity of stack exceeded (Max " + str(self.capacity) + " ) "
        self.item[self.top_element + 1] = element
        self.top_element += 1

    def pop(self):
        """pop top element of the stack"""
        assert self.top_element >= 0, "you cant pop an empty list"
        value = self.item[self.top_element] 
        self.item[self.top_element] = 0
        self.top_element -= 1
        return value

    def peek(self):
        "peek the top element in the stack"
        assert self.top_element >= 0, "There is no element in this stack"
        return self.item[self.top_element]

if __name__ == "__main__":
    test = Fixedstack(3)
    test.push(7)
    print(test.item)
    test.pop()
    print(test.item)