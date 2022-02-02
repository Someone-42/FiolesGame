from Stack import*

class Game:
    def __init__(self):
        self.vials = []
        self.moves = Stack()

    def try_move(self, a, b):
        if self.vials.can_move_into(self.vials[a], self.vials[b]):
            self.vials.move_into(self.vials[a], self.vials[b])
            return True
        return False

    def is_finished(self):
        i = 0
        while self.vials[i].is_complete() or self.vials[i]._is_empty():
            i += 1
            if i == (len(self.vials))-1:
                return True
        return False