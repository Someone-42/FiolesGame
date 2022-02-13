class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        assert self.items
        return self.items.pop()
    
    def peek(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)
    
    def clear(self):
        self.items.clear()
        