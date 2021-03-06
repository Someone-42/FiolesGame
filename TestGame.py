from Game import *
from UI import *
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

def run():
    game = Game()
    game.vials = get_test_level()
    start(1200,900,"test")
    load_game(game) 
    while not game.is_finished():
        display_game(game)
        input_value = poll_input(game)
        input_type = input_value[0]
        if input_type == InputType.QUIT:
            print("quitting")
            break
        elif input_type == InputType.MOVE:
            (_, i1, i2) = input_value
            if not game.try_move(i1, i2):
                show_invalid_move()
        elif input_type == InputType.UNDO:
            print("should be undoing")
    print("finished game")
        
if __name__ == "__main__":
    run()