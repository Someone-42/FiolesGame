class Move():
    def __init__(self, vial1, vial2, quantity):
        self.vial1, self.vial2, self.quantity = vial1, vial2, quantity

    def undo(self):
        self.vial2.force_move(self.vial1, self.quantity)