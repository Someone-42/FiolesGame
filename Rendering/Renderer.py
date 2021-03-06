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

__VIALS_POS = []

__BUTTONS = []
__LABELS = {}

__LAST_MOVE_WAS_INVALID = False

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

def load_game(game):
    global __VIAL_COUNT
    __VIAL_COUNT = len(game.vials)
    _bake_vials_rect(len(game.vials))

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

    buttons = [__RENDER_SETTINGS.quit_button, __RENDER_SETTINGS.undo_button, __RENDER_SETTINGS.reload_button]

    for i, button in enumerate(buttons):
        button.model.set_baked_rect(
            Rectangle2(
                button.rect.pos.mul_comp(__WINDOW_SIZE),
                button.rect.size.mul_comp(__WINDOW_SIZE)
            )
        )

    global __BUTTONS
    __BUTTONS = buttons

    labels = {
        "invalid" : __RENDER_SETTINGS.invalid_move_label
    }

    global __LABELS

    for key in labels.keys():
        label = labels[key]
        label.model.set_baked_rect(
            Rectangle2(
                label.rect.pos.mul_comp(__WINDOW_SIZE),
                label.rect.size.mul_comp(__WINDOW_SIZE)
            )
        )
        __LABELS[key] = label

def _bake_vials_rect(vial_count):
    vial_max_size_x_px = __VIAL_RECT_PX.size.x / __RENDER_SETTINGS.vials_per_row # We only calculate the size on the x axis, as the y axis size will depend on how many vials there are
    vial_spacing_x_px = vial_max_size_x_px * (__RENDER_SETTINGS.vial_spacing / 2)
    vial_size_x_px = vial_max_size_x_px - vial_spacing_x_px + (vial_spacing_x_px / __RENDER_SETTINGS.vials_per_row)

    rows = ((vial_count - 1) // (__RENDER_SETTINGS.vials_per_row)) + 1
    # Calculating y sizes and values
    vial_max_size_y_px = __VIAL_RECT_PX.size.y / rows
    vial_spacing_y_px = vial_max_size_y_px * (__RENDER_SETTINGS.row_spacing / 2)
    vial_size_y_px = vial_max_size_y_px - vial_spacing_y_px + (vial_spacing_y_px / rows)

    __VIALS_POS.clear()

    __RENDER_SETTINGS.vial_model.set_baked_size(Vector2(vial_size_x_px, vial_size_y_px))

    for i in range(vial_count):
        xi = i % __RENDER_SETTINGS.vials_per_row # Getting the column or x position
        yi = rows - 1 - (i // __RENDER_SETTINGS.vials_per_row) # Reversing so we fill up from the top
        __VIALS_POS.append(Vector2(
                xi * (vial_size_x_px + vial_spacing_x_px) + __VIAL_RECT_PX.pos.x,
                yi * (vial_size_y_px + vial_spacing_y_px) + __VIAL_RECT_PX.pos.y))

def clear():
    g.remplir_fenetre(__RENDER_SETTINGS.clear_color.to_tuple_rgb())

def render():
    g.affiche_tout()

def render_UI(game):
    #g.affiche_rectangle_plein(__UI_RECT_PX.pos.to_tuple(), (__UI_RECT_PX.pos + __UI_RECT_PX.size).to_tuple(), (200, 200, 0)) # Layout debug
    __BUTTONS[1].model.set_count(len(game.moves)) # Setting the count of undo button to the len of the moves
    for button in __BUTTONS:
        # Render every button
        button.model.render(button)

def render_vials(vials):
    #g.affiche_rectangle_plein(__VIAL_RECT_PX.pos.to_tuple(), (__VIAL_RECT_PX.pos + __VIAL_RECT_PX.size).to_tuple(), (0, 200, 0)) # Layout debug
    for vi, vial in enumerate(vials):
        __RENDER_SETTINGS.vial_model.render(vial, __VIALS_POS[vi], __SELECTED_VIAL_INDEX == vi)

def _render_invalid_move():
    if __LAST_MOVE_WAS_INVALID:
        label = __LABELS["invalid"]
        label.model.render()

def render_all(game):
    clear()
    render_UI(game)
    render_vials(game.vials)
    _render_invalid_move()
    render()
    global __LAST_MOVE_WAS_INVALID
    __LAST_MOVE_WAS_INVALID = False

def poll_inputs(game) -> tuple:
    """ Returns the treated input from a click or other user input """
    global __SELECTED_VIAL_INDEX

    # I know a state machine here would be wise but im too lazy
    def _can_select(vial):
        if __SELECTED_VIAL_INDEX is None:
            return not (vial.is_empty() or vial.is_complete())
        return (vial.is_empty()) or (not vial.is_complete())

    while True: # Continue asking for input till we get an input can be returned
        _x, _y = g.wait_clic()
        click = Vector2(_x, _y)

        if __VIAL_RECT_PX.is_point_inside(click):
            index = None
            for i, vial_p in enumerate(__VIALS_POS):
                vial = game.vials[i]
                vial_r = Rectangle2(vial_p, __RENDER_SETTINGS.vial_model.baked_size)
                if vial_r.is_point_inside(click) and _can_select(vial):
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
            for button in __BUTTONS:
                if button.is_click_on_button(click):
                    return button.on_click(button)
        else:
            __SELECTED_VIAL_INDEX = None
        
        render_all(game)

def render_new_invalid_move():
    global __LAST_MOVE_WAS_INVALID
    __LAST_MOVE_WAS_INVALID = True