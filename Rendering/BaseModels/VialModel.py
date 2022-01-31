from Rendering.Core import *
import Rendering.graphics as g

class VialModel:
    __slots__=(
        "colors",
        "line_color"
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
    
    def render(self, vial, rect):
        color_size_y = rect.size.y / (len(vial) + 0.5)
        for i, liquid in enumerate(vial.content):
            if not liquid:
                break
            g.affiche_rectangle_plein(
                (rect.pos + Vector2(color_size_y * i, 0)).to_tuple(),
                (rect.pos + Vector2(rect.size.x, color_size_y * (i + 1))).to_tuple(),
                self.colors[liquid]
            )
            
        points = rect.get_points4()
        for i in range(3):
            g.affiche_ligne(points[i], points[i+1], self.line_color)