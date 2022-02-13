from Stack import*
from Move import Move

class Game:
    def __init__(self):
        self.vials = []
        self.moves = Stack()

    def try_move(self, a, b):
        if self.vials[a].can_move_into(self.vials[b]):
            q = self.vials[a].move_into(self.vials[b])
            self.moves.push(Move(self.vials[a], self.vials[b], q))
            return True
        return False

    def is_finished(self):
        i = 0
        while self.vials[i].is_complete() or self.vials[i].is_empty():
            if i == (len(self.vials)) - 1:
                return True
            i += 1
        return False

    def undo_move(self):
        if self.moves.is_empty():
            return False
        self.moves.pop().undo()
        return True
