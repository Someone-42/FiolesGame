from Rendering.Core import *
import Rendering.graphics as g
from Rendering.BaseModels.SpriteModel import SpriteModel, SpriteFitMode


class ButtonModel:
    __slots__ = ("baked_rect")
    def __init__(self):
        self.baked_rect = None

    def render(self, button):
        pass

    def set_baked_rect(self, rect):
        self.baked_rect = rect

class SpriteButtonModel(ButtonModel):
    __slots__ = ("sprite_model")
    def __init__(self, sprite_model):
        self.sprite_model = sprite_model
        super().__init__()

    def set_baked_rect(self, rect): 
        self.baked_rect = rect
        self.sprite_model.set_baked_rect(rect)

    def render(self, button):
        #g.affiche_rectangle_plein(
        #    self.baked_rect.pos.to_tuple(),
        #    (self.baked_rect.pos + self.baked_rect.size).to_tuple(),
        #    (255, 0, 0)
        #)
        self.sprite_model.render()


class UndoButtonModel(ButtonModel):
    __slots__=("label_model", "sprite_model")
    def __init__(self, label_model):
        self.label_model = label_model
        self.sprite_model = SpriteModel("./Assets/Images/UndoArrow.png", Vector2(512, 512), SpriteFitMode.STRETCH)
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
        #    (0, 255, 0))
        self.sprite_model.render()
        self.label_model.render()
