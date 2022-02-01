from Stack import*

class Game:
    def __init__(self):
        self.vials = []
        self.moves = Stack()

    def try_move(self, a, b):
        if peut_deplacer_dans(a, b):
            deplacer_dans(a, b)
            return True
        return False

    def is_finished(self):
        i = 0
        while self.vials[i].est_complete() or self.vials[i].est_vide():
            i += 1
            if self.vials[-1] == self.vials[i]:
                return True
        return False
