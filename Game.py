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
        for i in self.vials:
            if self.vials[i].est_complete() or self.vials[i].est_vide():
                end = True
            else:
                end = False
            return end