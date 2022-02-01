import UI as ui
import Rendering.Renderer as r
import Rendering.graphics as g

if __name__ == "__main__":
    ui.start(1100, 800, "A testing thingy")
    r.load_game(12)
    while g.pas_echap():
        r.clear()
        r.render_vials([None] * 12)
        r.render_UI()
        r.render()