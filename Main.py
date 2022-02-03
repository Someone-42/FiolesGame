from Game import*
from UI import*

game = Game()

def run():
    start(1920,1080,"glass")
    while not game.is_finished():
        display_game(game)
        (i1, i2) = wait_for_move()
        if not game.try_move(i1, i2):
            show_invalid_move()
        
if __name__ == "__main__":
    run()