import Rendering.Renderer as r
import Rendering.RenderSettings as rs
from Rendering.Core import *
#from Rendering.SoundManager import *

UserInputType = InputType

def start(width, height, title = "A window"):
    r.init()
    r.create_window(width, height, title)
    r.load_settings(rs.RenderSettings(
        vials_per_row = 6, 
        margin_size = 0.04,
        vial_spacing = 0.7,
        row_spacing = 0.5,
        vial_rect = Rectangle2(Vector2(0, 0.15), Vector2(1, 0.85)),
        ui_rect = Rectangle2(Vector2(0, 0), Vector2(1, 0.15)),
        clear_color = Color(42, 42, 42)))

def load_game(game):
    r.load_game(game)

def display_game(game):
    r.render_all(game)

def show_invalid_move():
    r.render_new_invalid_move()
    r._render_invalid_move()
    r.render()

def poll_input(game) -> tuple:
    return r.poll_inputs(game)