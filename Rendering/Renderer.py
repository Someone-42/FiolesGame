#### Default Game Renderer ####
import Rendering.graphics as g
from Rendering.Core import *

"""

Screen Space : Coordinates on screen from 0 to 1
Screen coordinates : Coordinates on screen from 0 to Width for x and 0 to Height for y

"""

__RENDER_SETTINGS = None
__WINDOW_SIZE = None

__VIAL_COUNT = None
__SELECTED_VIAL_INDEX = None

__VIAL_RECT_PX = None
__UI_RECT_PX = None

__VIAL_RECTS = []

__BUTTONS = []

def __sc_to_ss(v: Vector2) -> Vector2:
    """ Returns Screen Coordinates vector to Screen Space """
    return v.div_comp(__WINDOW_SIZE)

def __ss_to_sc(v: Vector2) -> Vector2:
    """ Returns Screen Space vector to Screen Coordinates """
    return v.mul_comp(__WINDOW_SIZE)

def init():
    """ Initializes the renderer. Not initializing will cause bugs or crashes """
    g.affiche_auto_off()

def load_settings(render_settings):
    """ Loads settings and themes, calling it again will change the settings """
    global __RENDER_SETTINGS
    __RENDER_SETTINGS = render_settings
    _bake()
    if __VIAL_COUNT:
        _bake_vials_rect(__VIAL_COUNT)

def load_game(vial_count):
    global __VIAL_COUNT
    __VIAL_COUNT = vial_count
    _bake_vials_rect(vial_count)

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

def _bake_vials_rect(vial_count):
    vial_max_size_x_px = __VIAL_RECT_PX.size.x / __RENDER_SETTINGS.vials_per_row # We only calculate the size on the x axis, as the y axis size will depend on how many vials there are
    vial_spacing_x_px = vial_max_size_x_px * (__RENDER_SETTINGS.vial_spacing / 2)
    vial_size_x_px = vial_max_size_x_px - vial_spacing_x_px + (vial_spacing_x_px / __RENDER_SETTINGS.vials_per_row)

    rows = ((vial_count - 1) // (__RENDER_SETTINGS.vials_per_row)) + 1
    # Calculating y sizes and values
    vial_max_size_y_px = __VIAL_RECT_PX.size.y / rows
    vial_spacing_y_px = vial_max_size_y_px * (__RENDER_SETTINGS.row_spacing / 2)
    vial_size_y_px = vial_max_size_y_px - vial_spacing_y_px + (vial_spacing_y_px / rows)

    __VIAL_RECTS.clear()

    for i in range(vial_count):
        xi = i % __RENDER_SETTINGS.vials_per_row # Getting the column or x position
        yi = rows - 1 - (i // __RENDER_SETTINGS.vials_per_row) # Reversing so we fill up from the top
        __VIAL_RECTS.append(Rectangle2(
            Vector2(
                xi * (vial_size_x_px + vial_spacing_x_px) + __VIAL_RECT_PX.pos.x,
                yi * (vial_size_y_px + vial_spacing_y_px) + __VIAL_RECT_PX.pos.y),
            Vector2(
                vial_size_x_px,
                vial_size_y_px)))

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
    
    #g.affiche_rectangle_plein(__VIAL_RECT_PX.pos.to_tuple(), (__VIAL_RECT_PX.pos + __VIAL_RECT_PX.size).to_tuple(), (0, 200, 0)) # Layout debug

    for vi, vial in enumerate(vials):
        vial_rect = __VIAL_RECTS[vi]
        if __SELECTED_VIAL_INDEX == vi:
            # Show it is selected
            #g.affiche_rectangle( # Debug rectangle
            #    vial_rect.pos.to_tuple(),
            #    (vial_rect.pos + vial_rect.size).to_tuple(),
            #    (0, 0, 0), 8) # Dummy rendering color
            vial_rect = Rectangle2(vial_rect.pos - (vial_rect.size * 0.15), vial_rect.size * 1.3) # 30% size increase when vial selected
        __RENDER_SETTINGS.vial_model.render(vial, vial_rect)

def render_all(vials):
    clear()
    render_UI()
    render_vials(vials)
    render()

def poll_inputs(vials) -> tuple:
    """ Returns the treated input from a click or other user input """
    global __SELECTED_VIAL_INDEX

    while True: # Continue asking for input till we get an input can be returned
        _x, _y = g.wait_clic()
        click = Vector2(_x, _y)

        if __VIAL_RECT_PX.is_point_inside(click):
            index = None
            for i, vial in enumerate(__VIAL_RECTS):
                if vial.is_point_inside(click):
                    index = i
                    break
            if __SELECTED_VIAL_INDEX is None: # Selecting first vial
                __SELECTED_VIAL_INDEX = index
            else: # Else we already have a vial selected
                if __SELECTED_VIAL_INDEX == index: # Deselecting if the user clicked on the vial again
                    __SELECTED_VIAL_INDEX = None
                elif index != None: # Selecting the other vial
                    ret = (InputType.MOVE, __SELECTED_VIAL_INDEX, index)
                    __SELECTED_VIAL_INDEX = None
                    return ret

        elif __UI_RECT_PX.is_point_inside(click):
            # Go over every button in the UI rect and return which action was pressed
            __SELECTED_VIAL_INDEX = None

        else:
            __SELECTED_VIAL_INDEX = None
        
        render_all(vials)