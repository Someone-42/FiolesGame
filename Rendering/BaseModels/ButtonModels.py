from Rendering.Core import *
import Rendering.graphics as g

class ButtonModel:
    __slots__ = ("baked_rect")
    def __init__(self):
        self.baked_rect = None

    def render(self, button):
        pass

    def set_baked_rect(self, rect):
        self.baked_rect = rect

class QuitButtonModel(ButtonModel):
    __slots__ = ("color")
    def __init__(self, color = Color(255, 0, 0)):
        self.color = color
        super().__init__()

    def render(self, button):
        g.affiche_rectangle_plein(
            self.baked_rect.pos.to_tuple(),
            (self.baked_rect.pos + self.baked_rect.size).to_tuple(),
            self.color.to_tuple_rgb()
        )