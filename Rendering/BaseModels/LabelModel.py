from Rendering.Core import *
import Rendering.graphics as g

def _get_text_size(text, font_size, font):
    """ Return a vector 2 giving the width and the height of the text in screen coordinates *1 """
    return Vector2(
        g.largeur_texte(text, font_size, font), 
        g.hauteur_texte(text, font_size, font))

def _get_optimal_font_size(text, size, font):
    txt_size = _get_text_size(text, 42, font)
    v_ratio = txt_size / 42
    v_opt = size.div_comp(v_ratio)
    return int(min(v_opt.x, v_opt.y))

class LabelModel:
    __slots__=(
        "_text",
        "color",
        "_font",
        "baked_rect",
        "_font_size"
    )
    def __init__(self, text, color = Color(255, 255, 255), font = "arial"):
        self.color = color
        self._font = font
        self.baked_rect = None
        self._font_size = 42
        self._text = text

    def set_baked_rect(self, baked_rect):
        self.baked_rect = baked_rect
        self._recalculate()

    def _recalculate(self):
        if self.baked_rect is None:
            raise Error("Cannot recalculate without a size defined")
        self._font_size = _get_optimal_font_size(self._text, self.baked_rect.size, self._font)

    def set_text(self, text):
        old_text = self._text
        self._text = text
        if len(old_text) != len(text):
            self._recalculate()

    def render(self):
        g.affiche_texte(self._text, self.baked_rect.pos.to_tuple(), self.color.to_tuple_rgb(), self._font_size, self._font)