import UI as ui
import Rendering.Renderer as r
import Rendering.graphics as g

if __name__ == "__main__":
    ui.start(1150, 900, "A testing thingy")
    while g.pas_echap():
        r.clear()
        r.render_vials([None] * 12)
        r.render_UI()
        r.render()