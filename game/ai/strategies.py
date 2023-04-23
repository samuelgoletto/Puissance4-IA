from game.entities import Board

import random


def random_strategy(board: Board) -> int:
    """Random selection strategy"""

    remaining = list(range(7))
    remaining.remove(choice := random.choice(remaining))
    while board.is_column_full(choice) and remaining:  # si la colonne est pleine, on recommence
        remaining.remove(choice := random.choice(remaining))

    return choice  # Choice could be invalid if the board is already full


def interactive_strategy(board: Board) -> int:
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