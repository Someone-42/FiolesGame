import Rendering.Core as core
from Rendering.BaseModels.VialModels import VialModel
from Rendering.BaseModels.ButtonModels import QuitButtonModel, UndoButtonModel
from Rendering.BaseModels.LabelModel import LabelModel

def _quit_button_return(self):
    return (core.InputType.QUIT,)

def _undo_button_return(self):
    return (core.InputType.UNDO,)

class RenderSettings:
    __slots__=(
        "clear_color",
        "vials_per_row",
        "margin_size",
        "vial_spacing",
        "row_spacing",
        "vial_rect",
        "ui_rect",
        "vial_model",
        "quit_button",
        "undo_button",
        "invalid_move_label"
        )
    def __init__(self, vials_per_row = 6, 
        margin_size = 0.025, 
        vial_spacing = 0.7, 
        row_spacing = 0.5, 
        vial_rect = core.Rectangle2(core.Vector2(0, 0.15), 
        core.Vector2(1, 0.85)), 
        ui_rect = core.Rectangle2(core.Vector2(0, 0), 
        core.Vector2(1, 0.15)), 
        clear_color=core.Color(0, 0, 0), 
        vial_model=VialModel(line_color=core.Color(210, 220, 240)),
        invalid_move_label=core.Label(core.Rectangle2(core.Vector2(0.05, 0.15 * 0.15), core.Vector2(0.30, 0.15 * 0.75)), LabelModel("Invalid move", core.Color(210, 10, 0))),
        quit_button=core.Button(core.Rectangle2(core.Vector2(0.85, 0), core.Vector2(0.15, 0.15)), QuitButtonModel(), _quit_button_return),
        undo_button=core.Button(core.Rectangle2(core.Vector2(0.40, 0), core.Vector2(0.20, 0.15)), UndoButtonModel(LabelModel(" "), core.Color(142, 200, 10)), _undo_button_return)
        ):
        """ Creates a class with rendering settings for the renderer to use - margin_size has to be in screen space (from 0 to 1) - vial_spacing is a fraction of a vial_size.x """
        self.clear_color = clear_color
        self.vials_per_row = vials_per_row
        self.margin_size = margin_size
        self.vial_spacing = vial_spacing
        self.row_spacing = row_spacing
        self.ui_rect = ui_rect
        m_v = core.Vector2(margin_size, margin_size)
        self.vial_rect = core.Rectangle2(vial_rect.pos + m_v, vial_rect.size - (m_v * 2))
        self.vial_model = vial_model
        self.quit_button = quit_button
        self.undo_button = undo_button
        self.invalid_move_label = invalid_move_label