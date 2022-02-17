from Game import *
from Stack import *
from Vial import *
from Parser import *
import UI as ui

def run():
    levels = Parser("./Content/Levels1.txt")

    level = 1 # The level we want to load

    game = Game()
    game.vials = levels.load_level(level)

    ui.start(1200, 900, "Fioles Game 1.0")
    ui.load_game(game)

    while not game.is_finished():
        ui.display_game(game)
        i = ui.poll_input(game)
        if i[0] == ui.UserInputType.MOVE:
            if not game.try_move(i[1], i[2]):
                ui.show_invalid_move()
        elif i[0] == ui.UserInputType.QUIT:
            break
        elif i[0] == ui.UserInputType.UNDO:
            game.undo_move()
        elif i[0] == ui.UserInputType.RELOAD:
            game.vials = levels.load_level(level)
            game.moves.clear()
    print("You won (if you didn't quit)") # No ui for winning yet (No menus)
        
if __name__ == "__main__":
    run()


#s = Sound('tetris-theme-officiel.mp3')
#s.play(True)