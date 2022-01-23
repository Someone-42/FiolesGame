class Vial:

    def __init__(self, content, size):
        self.size = 4
        self.content = [0] * self.size
        self.last_index = self.content[-1]

    def _is_empty(self):
        """return True is the vial is empty, else return False"""
        pass

    def _top_color_count(self):
        """return top color's size in the vial"""
        pass


    def _place_free(self):
        """return free place in the vials"""
        pass

    def move_into(self, vial_2):
        """move vial 1 last color in vial 2 """
        pass

    def can_move_into(self, vial_2):
        """return True if the move is possible, else return False"""
        pass

    def is_complete(self,):
        """return True is the vial is complete, else return False"""
        pass