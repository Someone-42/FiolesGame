from Rendering.Core import *
import Rendering.graphics as g
from Rendering.BaseModels.SpriteModel import SpriteModel

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

class UndoButtonModel(ButtonModel):
    __slots__=("color", "label_model", "sprite_model")
    def __init__(self, label_model, color = Color(40, 190, 60)):
        self.color = color
        self.label_model = label_model
        self.sprite_model = SpriteModel("./Assets/Images/UndoArrow.png", Vector2(512, 512))
        super().__init__()

    def set_baked_rect(self, rect):
        self.baked_rect = rect
        text_rect = Rectangle2(rect.pos + (rect.size * 0.15), rect.size * 0.7)
        self.label_model.set_baked_rect(text_rect)
        self.sprite_model.set_baked_rect(rect)

    def set_count(self, count):
        s = str(count)
        if count == 0:
            s = ' '
        self.label_model.set_text(s)

    def render(self, button):
        #g.affiche_rectangle(
        #    self.baked_rect.pos.to_tuple(), 
        #    (self.baked_rect.pos + self.baked_rect.size).to_tuple(),
        #    self.color.to_tuple_rgb())
        self.sprite_model.render()
        self.label_model.render()
