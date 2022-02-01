from Stack import*

class Game:
    def __init__(self):
        self.vials = []
        self.moves = Stack()

    def try_move(self, a, b):
        if peut_deplacer_dans(a, b):
            deplacer_dans(a, b)
        return False

    def is_finished(self):
        pass