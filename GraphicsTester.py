import UI as ui
import Rendering.Renderer as r
import Rendering.graphics as g

if __name__ == "__main__":
    ui.start(1100, 800, "A testing thingy")
    r.load_game(12)
    vials = [None] * 12
    while g.pas_echap():
        r.render_all(vials)
        print(r.poll_inputs(vials))