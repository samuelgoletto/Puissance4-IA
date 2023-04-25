from typing import Callable, Union

from game.util import Box
from game.exceptions import *


# For type annotation on these type's method's parameters
class Board: pass
class Player: pass


class Player:
    players = {'0': None}

    def __new__(cls, id: str, /, *, strategy: Callable = None) -> Player:
        """Makes sure there is only unique instances of this type, uniqueness being based on their `id`"""

        if id in Player.players:
            return Player.players[id]

        Player.players[id] = player = object.__new__(cls)
        player.id = id
        player.strategy = strategy
        return player

    def __repr__(player) -> str:
        return f'{type(player).__name__}({player.id})'

    def __str__(player) -> str:
        return str(player.id)

    def delete(player) -> None:
        del Player.players[player.id]

    def choose_column_to_play(player, board: Board) -> int:
        return player.strategy(board, player)


class Board:
    def __init__(board, from_: Union[str, list[list[Union[Player, None]]]] = None) -> None:
        """Création du plateau selon deux options :
        * Création d'un plateau vide
        * Création d'un plateau à partir d'un `str` contenant l'enchaînement de chaque ligne
            * Transforme la chaine de 42 caractères en un tableau à 2 dimensions de 6 lignes et 7 colonnes
            * chaque sous-chaine de 6 caractères correspond à une ligne"""
        if from_ is None:
            board.inner = [[None] * 7 for _line in range(6)]
        elif type(from_) is list:  # Copy
            board.inner = from_
        elif type(from_) is str:
            board.input = from_
            try:
                board.inner = [[Player(from_[5 - i + j * 6]) for j in range(7)] for i in range(6)]
            except IndexError:
                board.inner = [[None] * 7 for k in range(6)]  # Error
        else:
            raise TypeError(f'Cannot instantiate `{type(board).__name__}` from `{type(from_).__name__}`')

    def copy(board) -> Board:
        return Board([list(row) for row in board.inner])

    def validate(board) -> None:
        if hasattr(board, "input"):
            if (length := len(board.input)) != 42:
                raise InvalidFormatError(f'The given grid should be exactly 42, but contains {length} ' +
                                         'characters instead')

            if (invalid_chars := ''.join(sorted(set(board.input.replace('0', '').replace('h', '').replace('m', ''))))) != '':
                raise InvalidFormatError(f'The given grid should contains only characters in the sequence \'0hm\' ' +
                                         f'but contains invalid characters from this sequence: \'{invalid_chars}\'')

        for c_nbr, column in enumerate(zip(*board.inner)):
            c = column.count(None)
            if column[:c].count(None) != c:  # If empty cells other than on top of the column
                raise InvalidConfiguration(f'The grid has floating empty cells on column {c_nbr}')

        cells = []
        for row in board.inner:
            cells.extend(row)
        player_tokens, machine_tokens = cells.count(Player('h')), cells.count(Player('m'))
        if machine_tokens != (player_tokens - 1):  # Beginning grid
            raise InvalidConfiguration('The grid has an invalid number of token between the player and the machine.\n' +
                                       f'machine={machine_tokens} != player={player_tokens} -1')

    def __repr__(board) -> str:
        return board.inner.__repr__()

    def __str__(board) -> str:
        """Représentation en `str` du `Board`"""
        display = lambda cell: '.' if cell is None else str(cell)
        return Box.encapsulate('\n'.join(' '.join(map(display, line)) for line in board.inner))

    def __getitem__(board, item) -> list[Player]:
        return board.inner[item]

    def __setitem__(board, key, value) -> None:
        board.inner[key] = value

    def __iter__(board) -> iter:
        return iter(board.inner)

    def is_full(board) -> bool:
        """Returns:
        * False: if any 0 in the board
        * True: otherwise"""
        return all(map(all, board.inner))

    def is_column_full(board, column: int) -> bool:
        """If the column is full, the cell on top will contain something (so not false)"""
        return bool(board.inner[0][column])

    def play_in_column(board, column: int, player: Player) -> Board:
        """`player` making its move in the `column`"""
        for i in range(5, -1, -1):
            if board[i][column] is None:
                board[i][column] = player
                break
        return board

    def to_sequence(board) -> str:
        result = ''
        cell_to_str = lambda cell: '0' if cell is None else str(cell)
        for column in zip(*board.inner):  # columns
            result += ''.join(map(cell_to_str, column))[::-1]
        return result
