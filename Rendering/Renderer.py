#### Default Game Renderer ####
import Rendering.graphics as g
from Rendering.Core import *
"""

Screen Space : Coordinates on screen from 0 to 1
Screen coordinates : Coordinates on screen from 0 to Width for x and 0 to Height for y

"""

__RENDER_SETTINGS = None
__WINDOW_SIZE = None

__VIAL_RECT_PX = None
__UI_RECT_PX = None
__VIAL_SIZE_X_PX = -1
__VIAL_SPACING_X_PX = -1

def __sc_to_ss(v: Vector2) -> Vector2:
    """ Returns Screen Coordinates vector to Screen Space """
    return v.div_comp(__WINDOW_SIZE)

def __ss_to_sc(v: Vector2) -> Vector2:
    """ Returns Screen Space vector to Screen Coordinates """
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

def _bake():
    margins_px = Vector2.scalar(__WINDOW_SIZE.y) * __RENDER_SETTINGS.margin_size
    ui_rect_px = Rectangle2(
        __RENDER_SETTINGS.ui_rect.pos.mul_comp(__WINDOW_SIZE),
        __RENDER_SETTINGS.ui_rect.size.mul_comp(__WINDOW_SIZE))
    vials_rect_px = Rectangle2(
        __RENDER_SETTINGS.vial_rect.pos.mul_comp(__WINDOW_SIZE) + margins_px,
        __RENDER_SETTINGS.vial_rect.size.mul_comp(__WINDOW_SIZE) - (margins_px * 2))

    global __VIAL_RECT_PX, __UI_RECT_PX
    __VIAL_RECT_PX = vials_rect_px
    __UI_RECT_PX = ui_rect_px

    # Vial size bake
    vial_max_size_x_px = vials_rect_px.size.x / __RENDER_SETTINGS.vials_per_row # We only calculate the size on the x axis, as the y axis size will depend on how many vials there are
    vial_spacing_x_px = vial_max_size_x_px * (__RENDER_SETTINGS.vial_spacing / 2)
    vial_size_x_px = vial_max_size_x_px - vial_spacing_x_px + (vial_spacing_x_px / __RENDER_SETTINGS.vials_per_row)
    
    global __VIAL_SIZE_X_PX, __VIAL_SPACING_X_PX
    __VIAL_SPACING_X_PX = vial_spacing_x_px
    __VIAL_SIZE_X_PX = vial_size_x_px

    # Get optimal size to render all
    #    and store their bounding box, with the colors bouding boxes

def clear():
    g.remplir_fenetre(__RENDER_SETTINGS.clear_color.to_tuple_rgb())

def render():
    g.affiche_tout()

def render_UI():
    g.affiche_rectangle_plein(__UI_RECT_PX.pos.to_tuple(), (__UI_RECT_PX.pos + __UI_RECT_PX.size).to_tuple(), (200, 200, 0)) # Layout debug

def render_vials(vials):
    # Then iterate over them
    # Get vial render size
    # Render using default parameters
    g.affiche_rectangle_plein(__VIAL_RECT_PX.pos.to_tuple(), (__VIAL_RECT_PX.pos + __VIAL_RECT_PX.size).to_tuple(), (0, 200, 0)) # Layout debug

    for vi, vial in enumerate(vials):
        i = vi % __RENDER_SETTINGS.vials_per_row
        v_pos_x = i * (__VIAL_SIZE_X_PX + __VIAL_SPACING_X_PX) + __VIAL_RECT_PX.pos.x
        p1, p2 = __VIAL_RECT_PX.get_as_points()
        g.affiche_rectangle(
            (v_pos_x, p1.y),
            (v_pos_x + __VIAL_SIZE_X_PX, p2.y),
            (0, 0, 255), 8) # Dummy rendering color


def get_click() -> tuple:
    """ Returns a tuple in screen coordinates """
    return g.wait_clic()