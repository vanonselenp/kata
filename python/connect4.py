import pytest

# ## Description

# This game is played on a vertical board wich has seven hollow columns and six rows.
# Each column has a hole in the upper part of the board, where pieces are introduced.
# There is a window for every square, so that pieces can be seen from both sides.
# In short, it´s a vertical board with 42 windows distributed in 6 rows and 7 columns.
# Both players have a set of 21 thin pieces (like coins); each of them uses a different
# colour. The board is empty at the start of the game.

# ## Objective

# The aim for both players is to make a straight line of four own pieces; the line can
# be vertical, horizontal or diagonal.

# ## How the game goes on

# Before starting, players decide randomly which of them will be the beginner;
# * moves are made alternatively, one by turn.
# * Moves entails in placing new pieces on the board; pieces slide downwards from upper
# holes, falling down to the last row or piling up on the last piece introduced in
# the same column. So, in every turn the introduced piece may be placed at most on
# seven different squares.
# The winner is the first player who gets a straight line made with four own pieces
# and no gaps between them.


class Player:
    X = 'x'
    O = 'o'
    Empty = '_'


class Column:
    One = 0
    Two = 1
    Three = 2
    Four = 3
    Five = 4
    Six = 5
    Seven = 6


class Connect4:
    def __init__(self):
        self.board = Board()
        self.current_player = Player.X

    def get_current_player(self):
        return self.current_player

    def play_at(self, position):
        successfully_placed = self.board.place_at(position, self.current_player)

        if successfully_placed:
            self.switch_player()

    def switch_player(self):
        self.current_player = Player.X if self.current_player != Player.X else Player.O

    def get_board(self):
        return self.board.get_display()

    def get_winner(self):
        return self.board.get_winner()


class Board:
    def __init__(self):
        self.board = [
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty]
        ]
        self.determine_winner = DetermineWinner()

    def place_at(self, position, player):
        for row in range(5, -1, -1):
            if self.board[row][position] == Player.Empty:
                self.board[row][position] = player
                return True

        return False

    def get_display(self):
        return "\n".join(["".join(x) for x in self.board])

    def get_winner(self):
        return self.determine_winner.get_winner(self.board)


class DetermineWinner:
    def __init__(self):
        self.rules = Rules()

    @staticmethod
    def apply_rule(rule, board):
        rows, columns, applied_rule = rule
        for i in rows:
            for j in columns:
                if applied_rule(i, j, board):
                    return board[i][j]

    def get_winner(self, board):
        rules = self.rules.get_rules()

        winners = [self.apply_rule(rule, board) for rule in rules]

        print(winners)

        if Player.X in winners:
            return Player.X

        if Player.O in winners:
            return Player.O

        return None


class Rules:
    def get_rules(self):
        return [
            (range(5, -1, -1), range(0, 4), self.is_horizontal),
            (range(5, 2, -1), range(0, 7), self.is_vertical),
            (range(5, 2, -1), range(0, 4), self.is_right_diagonal),
            (range(5, 2, -1), range(3, 7), self.is_left_diagonal),
        ]

    @staticmethod
    def current_is_empty(current):
        return current == Player.Empty

    @staticmethod
    def is_vertical(row, column, board):
        current = board[row][column]
        return (
                not Rules.current_is_empty(current)
                and current
                == board[row - 1][column]
                == board[row - 2][column]
                == board[row - 3][column]
        )

    @staticmethod
    def is_horizontal(row, column, board):
        current = board[row][column]
        return (
            not Rules.current_is_empty(current)
            and current
            == board[row][column + 1]
            == board[row][column + 2]
            == board[row][column + 3]
        )

    @staticmethod
    def is_right_diagonal(row, column, board):
        current = board[row][column]
        return (
            not Rules.current_is_empty(current)
            and current
            == board[row - 1][column + 1]
            == board[row - 2][column + 2]
            == board[row - 3][column + 3]
        )

    @staticmethod
    def is_left_diagonal(row, column, board):
        current = board[row][column]
        return (
            not Rules.current_is_empty(current)
            and current
            == board[row - 1][column - 1]
            == board[row - 2][column - 2]
            == board[row - 3][column - 3]
        )


class TestConnect4:
    def test_player_x_is_the_first_player(self):
        connect = Connect4()

        assert Player.X == connect.get_current_player()

    def test_player_o_is_the_second_player(self):
        connect = Connect4()

        connect.play_at(Column.One)

        assert Player.O == connect.get_current_player()

    def test_player_x_follows_from_o(self):
        connect = Connect4()

        connect.play_at(Column.One)
        connect.play_at(Column.One)

        assert Player.X == connect.get_current_player()

    @pytest.mark.parametrize("expected,moves", [
        ("_______\n_______\n_______\n_______\n_______\nx______", [Column.One]),
        ("_______\n_______\n_______\n_______\n_______\n_x_____", [Column.Two]),
        ("_______\n_______\n_______\n_______\n_______\n__x____", [Column.Three]),
        ("_______\n_______\n_______\n_______\n_______\nxo_____", [Column.One, Column.Two]),
        ("_______\n_______\n_______\n_______\nx______\nxo_____", [Column.One, Column.Two, Column.One]),
        ("_______\n_______\n_______\nx______\no______\nx______", [Column.One, Column.One, Column.One]),
        ("o______\nx______\no______\nx______\no______\nx______",
         [Column.One, Column.One, Column.One, Column.One, Column.One, Column.One]),
        ("o______\nx______\no______\nx______\no______\nxx_____",
         [Column.One, Column.One, Column.One, Column.One, Column.One, Column.One, Column.One, Column.Two]),

    ])
    def test_board_to_look_like_given_a_set_of_moves(self, expected, moves):
        connect = Connect4()

        for move in moves:
            connect.play_at(move)

        print(connect.get_board())
        assert expected == connect.get_board()

    @pytest.mark.parametrize("winner,moves", [
        # (Player.X, [Column.One, Column.One, Column.Two, Column.Two, Column.Three, Column.Three, Column.Four]),
        (None, []),
        (Player.X, [Column.One, Column.One, Column.Two, Column.Two, Column.Three, Column.Three, Column.Four]),
        (Player.O,
         [Column.Seven, Column.One, Column.One, Column.Two, Column.Two, Column.Three, Column.Three, Column.Four]),
        (Player.X, [Column.Two, Column.One, Column.Three, Column.Two, Column.Four, Column.Three, Column.Five]),
        (Player.X, [Column.One, Column.Two, Column.One, Column.Three, Column.Two, Column.Four, Column.Three, Column.One,
                    Column.Four]),
        (Player.X, [Column.One, Column.Two, Column.One, Column.Two, Column.One, Column.Two, Column.One])
    ])
    def test_horizontal_wins(self, winner, moves):
        connect = Connect4()

        for move in moves:
            connect.play_at(move)

        print(connect.get_board())
        assert connect.get_winner() == winner

    def test_determine_none_winner(self):
        board = [
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty]
        ]

        assert DetermineWinner().get_winner(board) is None

    def test_determine_horizontal_winner(self):
        board = [
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.X, Player.X, Player.X, Player.X, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty]
        ]

        assert DetermineWinner().get_winner(board) is Player.X

    def test_determine_vertical_winner_column_1(self):
        board = [
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.X, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.X, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.X, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.X, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty]
        ]

        assert DetermineWinner().get_winner(board) is Player.X

    def test_determine_vertical_winner_column_2(self):
        board = [
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.X, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.X, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.X, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.X, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty]
        ]

        assert DetermineWinner().get_winner(board) is Player.X

    def test_determine_right_diagnonal_winner(self):
        board = [
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.X, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.X, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.X, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.X, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty]
        ]

        assert DetermineWinner().get_winner(board) is Player.X

    def test_determine_left_diagnonal_winner(self):
        board = [
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.X, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.X, Player.Empty, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.X, Player.Empty, Player.Empty, Player.Empty, Player.Empty],
            [Player.Empty, Player.Empty, Player.Empty, Player.X, Player.Empty, Player.Empty, Player.Empty]
        ]

        assert DetermineWinner().get_winner(board) is Player.X
