from game.util import Box

from typing import Callable, Union
import random


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
        player.strategy = strategy if strategy is not None else Player.default_strategy
        return player

    def __repr__(player) -> str:
        return f'{type(player).__name__}({player.id})'

    def __str__(player) -> str:
        return str(player.id)

    def delete(player) -> None:
        del Player.players[player.id]

    def choose_column_to_play(player, board: Board) -> int:
        return player.strategy(board)

    @staticmethod
    def default_strategy(board: Board) -> int:
        """Random selection strategy"""

        remaining = list(range(7))
        remaining.remove(choice := random.choice(remaining))
        while board.is_column_full(choice) and remaining:  # si la colonne est pleine, on recommence
            remaining.remove(choice := random.choice(remaining))

        return choice  # Choice could be invalid if the board is already full


class Board:
    def __init__(board, grid: list[list[Union[Player, None]]] = None) -> None:
        """Crée une instance de `Board` contenant un tableau 7×6 vide"""
        if grid is None:
            board.inner = [[None] * 7 for _line in range(6)]
        else:
            board.inner = grid

    @staticmethod
    def new(from_: str = None) -> Board:
        """Création du plateau selon deux options :
        * Création d'un plateau vide
        * Création d'un plateau à partir d'un `str` contenant l'enchaînement de chaque ligne
            * Transforme la chaine de 42 caractères en un tableau à 2 dimensions de 6 lignes et 7 colonnes
            * chaque sous-chaine de 6 caractères correspond à une ligne"""

        if from_ is None:  # Build a fresh new board
            return Board()

        return Board([[Player(from_[5 - i + j * 6]) for j in range(7)] for i in range(6)])

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

    def play_in_column(board, column: int, player: Player) -> None:
        """`player` making its move in the `column`"""
        for i in range(5, -1, -1):
            if board[i][column] is None:
                board[i][column] = player
                break

    def to_sequence(board) -> str:
        result = ''
        cell_to_str = lambda cell: '0' if cell is None else str(cell)
        for column in zip(*board.inner):
            result += ''.join(map(cell_to_str, column))[::-1]
        return result
