from Game import *
from UI import *
from Stack import *
from Vials import *

def get_test_level():
    vials = [Vial(4) for _ in range(10)]
    vials[0].push_content([1, 2])
    vials[1].push_content([4, 1, 4])
    vials[2].push_content([2, 3, 5])
    vials[3].push_content([2, 1, 1])
    vials[4].push_content([3, 2])
    vials[5].push_content([4, 3, 3])
    vials[6].push_content([2, 5, 5])
    vials[7].push_content([4, 2, 5])
    vials[8].push_content([2, 2])
    return vials

game = Game()
game.vials = get_test_level()

def run():
    start(1080,800,"glass")
    load_game(game)
    while not game.is_finished():
        display_game(game)
        i = poll_input(game)
        if i[0] == UserInputType.MOVE:
            if not game.try_move(i[1], i[2]):
                show_invalid_move()
        if i[0] == UserInputType.QUIT:
            break
        if i[0] == UserInputType.UNDO:
            game.undo_move()
    print('adios amigos hehe')
        
if __name__ == "__main__":
    run()