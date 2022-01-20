#### Default Game Renderer ####
import Rendering.graphics as g

__CLEAR_COLOR = g.couleur(0, 0, 0)

def init():
    g.affiche_auto_off()

def create_window(width, height, title = "A window"):
    g.init_fenetre(width, height, title)
    clear()

def clear():
    g.remplir_fenetre(__CLEAR_COLOR)

def render():
    g.affiche_tout()

def render_vials(vials):
    # Get optimal size to render all
    # Then iterate over them
    # Get vial render size
    # Render using default parameters
    pass