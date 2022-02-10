from Rendering.Core import *
import Rendering.graphics as g

class VialModel:
    __slots__=(
        "colors",
        "line_color",
        "baked_size"
    )
    def __init__(self, line_color = Color(255, 255, 255), colors = [
        Color(200, 0, 0),
        Color(0, 200, 0),
        Color(50, 80, 200),
        Color(150, 0, 220),
        Color(140, 140, 0),
        Color(200, 200, 230)
    ]):
        self.colors = colors
        self.line_color = line_color
        self.baked_size = None
    
    def set_baked_size(self, baked_size):
        self.baked_size = baked_size

    def render(self, vial, pos, selected: bool):
        size = self.baked_size
        line_size = 6
        if selected:
            pos = pos - (self.baked_size * 0.12)
            size = self.baked_size * 1.24       # Size increase of 24%
            line_size = 8
        color_size_y = size.y / (len(vial) + 0.5)
        for i, liquid in enumerate(vial.content):
            if not liquid:
                break
            g.affiche_rectangle_plein(
                (pos + Vector2(0, color_size_y * i - 2)).to_tuple(), # -2 so we have one more pixel down to render the full vial
                (pos + Vector2(size.x, color_size_y * (i + 1))).to_tuple(),
                self.colors[liquid].to_tuple_rgb()
            )
            
        points = Rectangle2(pos, size).get_points4()
        line_color_tuple = self.line_color.to_tuple_rgb()
        for i in range(3, 6):
            pi1 = i % 4
            pi2 = (i+1) % 4
            g.affiche_ligne(points[pi1].to_tuple(), points[pi2].to_tuple(), line_color_tuple, line_size)