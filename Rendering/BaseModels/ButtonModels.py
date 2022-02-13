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
        self.label_model.set_baked_rect(Rectangle2(rect.pos + Vector2(1, 0).mul_comp(rect.size) * 0.15, rect.size * 0.8))
        self.sprite_model.set_baked_rect(Rectangle2(
            rect.pos + rect.size.mul_comp(Vector2(0, 1)) * 0.6, 
            Vector2(rect.size.x, rect.size.y * 0.4)))

    def set_count(self, count):
        s = str(count)
        if count == 0:
            s = 'X'
        self.label_model.set_text(s)

    def render(self, button):
        #g.affiche_rectangle( # DEBUG RECT
        #    self.baked_rect.pos.to_tuple(), 
        #    (self.baked_rect.pos + self.baked_rect.size).to_tuple(),
        #    self.color.to_tuple_rgb())
        self.sprite_model.render()
        self.label_model.render()
