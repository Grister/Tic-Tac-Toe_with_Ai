def convert_in_index(first, second):  # преобразование координат в индексы
    return ((int(first) - 1) * 3) + (int(second) + 2) - 3


def correct_input(coordinates, grid):  # проверка на правильность ввода координат
    if coordinates[0].isdigit() and coordinates[1].isdigit():
        if coordinates[0] in '123' and coordinates[1] in '123':
            position = convert_in_index(coordinates[0], coordinates[1])
            if grid[position] != ' ':  # проверка на занятую ячейку
                print("This cell is occupied! Choose another one!")
                return False
            else:
                return True
        else:
            print("Coordinates should be from 1 to 3!")
            return False
    else:
        print("You should enter numbers!")
        return False


def user(board):
    cord = input('Enter the coordinates: ').split()
    if correct_input(cord, board):
        return convert_in_index(*cord)
    user(board)
