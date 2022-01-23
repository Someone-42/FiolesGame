#### Default Game Renderer ####
import Rendering.graphics as g
from Rendering.Core import Vector2
"""

Screen Space : Coordinates on screen from 0 to 1
Screen coordinates : Coordinates on screen from 0 to Width for x and 0 to Height for y

"""

__RENDER_SETTINGS = None
__WINDOW_SIZE = None

def __sc_to_ss(v: Vector2) -> Vector2:
    """ Returns Screen Coordinates tuple to Screen Space """
    return v.div_comp(__WINDOW_SIZE)

def __ss_to_sc(v: Vector2) -> Vector2:
    """ Returns Screen Space tuple to Screen Coordinates """
    return v.mul_comp(__WINDOW_SIZE)

def init():
    """ Initializes the renderer. Not initializing will cause bugs or crashes """
    g.affiche_auto_off()

def load(render_settings):
    """ Loads settings and themes, calling it again will change the settings """
    global __RENDER_SETTINGS
    __RENDER_SETTINGS = render_settings
    _bake()

def create_window(width, height, title = "A window"):
    global __WINDOW_SIZE
    __WINDOW_SIZE = Vector2(width, height)
    g.init_fenetre(width, height, title)
    clear()

def _bake():
    """ Bakes rendering to simplify render step """
    # Get optimal size to render all
    #    and store their bounding box, with the colors bouding boxes

def clear():
    g.remplir_fenetre(__RENDER_SETTINGS.clear_color.to_tuple_rgb())

def render():
    g.affiche_tout()

def render_vials(vials):
    # Then iterate over them
    # Get vial render size
    # Render using default parameters
    pass
def get_click() -> tuple:
    """ Returns a tuple in screen space """
    pass