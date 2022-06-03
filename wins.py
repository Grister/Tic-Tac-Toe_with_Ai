class EndGameError(Exception):
    pass


def if_wins(option, squares):
    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])
    for combos in winning_combos:
        if squares[combos[0]] == option and \
                squares[combos[1]] == option and \
                squares[combos[2]] == option:
            print(f'{option} wins')
            raise EndGameError
    if " " not in squares.values():
        print("Draw")
        raise EndGameError
