import Rendering.Core as core

class RenderSettings:
    __slots__=(
        "clear_color",
        "vial_per_row",
        "margin_size",
        "vial_spacing"
        )
    def __init__(self, vial_per_row = 6, margin_size = 0.15, vial_spacing = 0.7, clear_color=core.Color(0, 0, 0)):
        """ Creates a class with rendering settings for the renderer to use - margin_size has to be in screen space (from 0 to 1) - vial_spacing is a fraction of a vial_size.x """
        self.clear_color = clear_color
        self.vial_per_row = vial_per_row
        self.margin_size = margin_size
        self.vial_spacing = vial_spacing