from minimax import TicTacToeBrain
from user import user
from wins import if_wins, EndGameError


def correct_args(func):
    start_option = {'user', 'easy', 'medium', 'hard'}

    def wrapper(*args):
        if {i for i in args}.issubset(start_option):
            func(*args)
        else:
            raise IndexError

    return wrapper


def move(option, lvl):
    if lvl == 'easy':
        print(f'Making move level "{lvl}"')
        game.make_move(game.easy(), option)
    elif lvl == 'medium':
        print(f'Making move level "{lvl}"')
        game.make_move(game.medium(option), option)
    elif lvl == 'hard':
        print(f'Making move level "{lvl}"')
        _, best_move = game.minimax(option)
        game.make_move(best_move, option)
    elif lvl == 'user':
        game.make_move(user(game.squares), option)

    game.show_board()
    if_wins(option, game.squares)


@correct_args
def start_game(player_one, player_two):
    game.create_board()
    game.show_board()
    try:
        while True:
            move(option='X', lvl=player_one)
            move(option='O', lvl=player_two)
    except EndGameError:
        pass


def main():
    command = input("Input command: ").split()
    if command[0] == 'exit':
        exit()
    elif command[0] == 'start':
        try:
            start_game(command[1], command[2])
        except IndexError:
            print('Bad parameters')
    else:
        print('Bad parameters')
    main()


if __name__ == '__main__':
    game = TicTacToeBrain()
    main()
