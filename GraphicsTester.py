import UI as ui
import Rendering.Renderer as r
import Rendering.graphics as g

if __name__ == "__main__":
    ui.start(1200, 800, "A testing thingy")
    while g.pas_echap():
        r.clear()
        r.render_vials([None] * 6)
        r.render_UI()
        r.render()