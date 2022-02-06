from Rendering.Core import *
import Rendering.graphics as g

class QuitButtonModel:
    __slots__ = ("color")
    def __init__(self, color = (255, 0, 0)):
        self.color = color

    def render(self, button, rect):
        g.affiche_rectangle_plein(
            rect.pos.to_tuple(),
            (rect.pos + rect.size).to_tuple(),
            self.color.to_tuple_rgb()
        )