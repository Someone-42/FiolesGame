class Vial:

    def __init__(self, size):
        self.size = size
        self.content = [0] * self.size
        self.top = -1

    def _top_color_count(self):
        """return top color's size in the vial"""
        if self._is_empty():
            return 0
        counter = 1
        while self.content[self.top] == self.content[self.top - counter]:
            counter += 1
        return counter

    def _place_free(self):
        """return free place in the vials"""
        return self.size - (self.top + 1)
    
    
    def is_empty(self):
        """return True is the vial is empty, else return False"""
        return self.top == -1

    def pop(self):
        value = self.content[self.top]
        self.content[self.top] = 0
        self.top -= 1
        return value

    def push(self, value):
        self.top += 1
        self.content[self.top] = value
        
    def move_into(self, other):
        """move vial 1 last color in vial 2 """
        k = min(self._top_color_count, other._place_free())
        for i in range(k):
            other.push(self.pop())
            
    def can_move_into(self, other):
        """return True if the move is possible, else return False"""
        if self.top + 1  == other.size() or self.content[self.top] != other.content[other.top]:
            return False

    def is_complete(self,):
        """return True is the vial is complete, else return False"""
        return self.content.count(self.content[0]) == len(self.content)          

