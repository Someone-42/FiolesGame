import Rendering.Renderer as r

def start(width, height, title = "A window"):
    r.init()
    r.create_window(width, height, title)

def display_game(game: Game):
    r.clear()
    r.render_vials(game.vials)
    r.render()

def wait_for_move() -> tuple:
    pass