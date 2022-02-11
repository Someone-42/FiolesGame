from Game import *
from UI import *
from Stack import *
from Vials import *
from Parser import *

levels = Parser("./Content/Levels1.txt")

game = Game()
game.vials = levels.load_level(1)

def run():
    start(1920,1080,"glass")
    load_game(game)
    while not game.is_finished():
        display_game(game)
        i = poll_input(game)
        if i[0] == UserInputType.MOVE:
            if not game.try_move(i[1], i[2]):
                show_invalid_move()
        elif i[0] == UserInputType.QUIT:
            break
        elif i[0] == UserInputType.UNDO:
            game.undo_move()
    print('adios amigos hehe')
        
if __name__ == "__main__":
    run()


#s = Sound('tetris-theme-officiel.mp3')
#s.play(True)