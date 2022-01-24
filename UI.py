import Rendering.Renderer as r
import Rendering.RenderSettings as rs
import Rendering.Core as core

def start(width, height, title = "A window"):
    r.init()
    r.create_window(width, height, title)
    r.load(rs.RenderSettings(6, 0.05, 0.7, core.Color(42, 42, 42)))

def display_game(game):
    r.clear()
    r.render_vials(game.vials)
    r.render()

def wait_for_move() -> tuple:
    pass