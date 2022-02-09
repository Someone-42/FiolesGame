import Rendering.Renderer as r
import Rendering.RenderSettings as rs
from Rendering.Core import *
from Rendering.SoundManager import *

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
    r.load_game(len(game.vials))

def display_game(game):
    r.clear()
    r.render_vials(game.vials)
    r.render_UI()
    r.render()

def show_invalid_move():
    print("you dumb fuck")

def poll_input(game) -> tuple:
    return r.poll_inputs(game.vials)