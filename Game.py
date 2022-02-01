from Stack import*

class Game:
    def __init__(self):
        self.vials = []
        self.moves = Stack()
        
    def try_moving(self, a, b):
        if self.vials[a]:
            if len(self.vials[b]) != 3:
                return True
        return False

    def is_finished(self):
        pass