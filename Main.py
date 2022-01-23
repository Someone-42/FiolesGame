from Game import*
from UI import*

game = Game()

def run():
    while not game.finished():
        display_game(game)
        (i1, i2) = wait_for_move()
        if not game.try_move(i1, i2):
            print("couldn't move")
        