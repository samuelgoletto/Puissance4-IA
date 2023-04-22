from game.ai import *
from game.util import Box

import random


class Board:
    def __init__(board):
        """Crée une instance de `Board` contenant un tableau 7×6 vide"""
        board.inner = [[0] * 7 for _line in range(6)]

    @staticmethod
    def new(from_: str = None):
        """Création du plateau selon deux options :
        * Création d'un plateau vide
        * Création d'un plateau à partir d'un `str` contenant l'enchaînement de chaque ligne
            * Transforme la chaine de 42 caractères en un tableau à 2 dimensions de 6 lignes et 7 colonnes
            * chaque sous-chaine de 6 caractères correspond à une ligne"""
        if from_ is None:  # Build a fresh new board
            return Board()

        board = []
        for i in range(6):
            column = []
            for j in range(7):
                column.append(from_[5 - i + j * 6])
            board.append(column)
        # remplace tous les h par des 1 et les m par des 2.
        for i in range(6):
            for j in range(7):
                if board[i][j] == 'h':
                    board[i][j] = 1
                elif board[i][j] == 'm':
                    board[i][j] = 2
                else:
                    board[i][j] = 0
        return board

    def __repr__(board) -> str:
        return board.__repr__()

    def __str__(board) -> str:
        """Représentation en `str` du `Board`"""
        display = lambda cell: '.' if cell == 0 else str(cell)
        return Box.encapsulate('\n'.join(' '.join(map(display, line)) for line in board.inner))

    def __getitem__(board, item) -> list:
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

    def is_column_full(board, column: int):
        """If the column is full, the cell on top will contain something (so not false)"""
        return board.inner[0][column]


def is_game_over(board: Board) -> bool:
    return is_winning_move(board, 1) or is_winning_move(board, 2) or board.is_full()


def play_in_column(board: Board, column: int, player: int) -> Board:
    # joue dans la colonne choisie
    for i in range(5, -1, -1):
        if board[i][column] == 0:
            board[i][column] = player
            break
    return board


def player_choose_column(board: Board) -> int:
    print("À toi de jouer !")
    while True:
        choice = input("Choisis une colonne (1-7) : ")
        # si ce n'est pas un chiffre entre 1 et 7, on recommence
        if not choice.isdigit() or (choice := int(choice)-1) not in range(7):
            print("Cette colonne n'existe pas !")
            continue
        # si la colonne est pleine, on recommence
        if board.is_column_full(choice):
            print("Cette colonne est pleine !")
            continue
        break
    # on renvoie la colonne choisie
    return choice


def ai_choose_column(board: Board) -> int:
    print("Au tour de l'IA...")
    while True:
        choice = random.randint(0, 6)
        # si la colonne est pleine, on recommence
        if board.is_column_full(choice):
            continue
        break
    # on renvoie la colonne choisie
    return choice
