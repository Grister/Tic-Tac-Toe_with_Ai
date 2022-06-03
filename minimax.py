import random


class TicTacToeBrain:
    def __init__(self):
        self._available_moves = None
        self._squares = {}
        self._winning_combos = (
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6])

    @staticmethod
    def get_enemy_player(player):
        if player == "X":
            return "O"
        return "X"

    def create_board(self):
        for i in range(9):
            self._squares[i] = " "

    def show_board(self):
        print('''---------''')
        print("|", self._squares[0], self._squares[1], self._squares[2], "|")
        print("|", self._squares[3], self._squares[4], self._squares[5], "|")
        print("|", self._squares[6], self._squares[7], self._squares[8], "|")
        print('''---------''')

    def get_available_moves(self):
        self._available_moves = []
        for i in range(9):
            if self._squares[i] == " ":
                self._available_moves.append(i)
        return self._available_moves

    def get_combos_in_board(self):
        cells = list(self._squares.values())
        return [cells[0:3], cells[3:6], cells[6::], cells[0::3],
                cells[1::3], cells[2::3], cells[0::4], cells[2:7:2]]

    def make_move(self, position, player):
        self._squares[position] = player

    def complete(self):
        if " " not in self._squares.values():
            return True
        if self.get_winner() is not None:
            return True
        return False

    def get_winner(self):
        for player in ("X", "O"):
            for combos in self._winning_combos:
                if self._squares[combos[0]] == player and \
                        self._squares[combos[1]] == player and self._squares[combos[2]] == player:
                    return player
        if " " not in self._squares.values():
            return "Draw"
        return None

    def close_position(self, player):
        combo_cells = self.get_combos_in_board()
        if [player, player, ' '] in combo_cells:
            pos = [self._winning_combos[n][-1] for n, x in enumerate(combo_cells) if x == [player, player, ' ']]
        elif [player, ' ', player] in combo_cells:
            pos = [self._winning_combos[n][1] for n, x in enumerate(combo_cells) if x == [player, ' ', player]]
        elif [' ', player, player] in combo_cells:
            pos = [self._winning_combos[n][0] for n, x in enumerate(combo_cells) if x == [' ', player, player]]
        return pos[0]

    def can_win(self, player):
        combo_cells = self.get_combos_in_board()
        if [player, player, ' '] in combo_cells or \
                [player, ' ', player] in combo_cells or \
                [' ', player, player] in combo_cells:
            return True
        return False

    def easy(self):
        computer_move = random.choice(self.get_available_moves())
        return int(computer_move)

    def medium(self, player):
        enemy_player = self.get_enemy_player(player)

        if self.can_win(player):
            return self.close_position(player)

        if self.can_win(enemy_player):
            return self.close_position(enemy_player)

        return self.easy()

    def minimax(self, player, depth=0):
        best_move = None
        if player == "O":
            best = -10
        else:
            best = 10
        if self.complete():
            if self.get_winner() == "X":
                return -10 + depth, None
            elif self.get_winner() == "Draw":
                return 0, None
            elif self.get_winner() == "O":
                return 10 - depth, None

        for move in self.get_available_moves():

            self.make_move(move, player)

            value, _ = self.minimax(self.get_enemy_player(player), depth + 1)

            self.make_move(move, " ")
            if player == "O":
                if value > best:
                    best, best_move = value, move
            else:
                if value < best:
                    best, best_move = value, move

        return best, best_move

    @property
    def squares(self):
        return self._squares


if __name__ == '__main__':
    game = TicTacToeBrain()
    game.create_board()

    game.make_move(0, 'X')
    game.make_move(2, 'X')
    game.make_move(3, 'O')
    game.make_move(7, 'O')
    game.make_move(game.medium('O'), 'O')
    game.show_board()

    # _, bestMove = game.minimax("O")
    # game.make_move(bestMove, 'O')
    # game.show_board()
    # _, bestMove = game.minimax("X")
    # game.make_move(bestMove, 'X')
    # game.show_board()
    # _, bestMove = game.minimax("O")
    # game.make_move(bestMove, 'O')
    # game.show_board()
    # _, bestMove = game.minimax("X")
    # game.make_move(bestMove, 'X')
    # game.show_board()
