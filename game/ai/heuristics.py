from game.entities import Board, Player

from typing import Union


def evaluate(board: Board, player: Player) -> float:
    score = 0

    # Ajoute du score si le joueur a des jetons sur la colonne du milieu
    center_array = tuple(zip(*board))[3]
    center_count = center_array.count(player)
    score += center_count * 3

    # Vérifier les alignements horizontaux
    for row in range(6):
        for col in range(4):
            pieces = board[row][col:col+4]
            score += evaluate_pieces(pieces, player)

    # Vérifier les alignements verticaux
    for row in range(3):
        for col in range(7):
            pieces = [board[row+i][col] for i in range(4)]
            score += evaluate_pieces(pieces, player)

    # Vérifier les alignements diagonaux (en haut à gauche vers le bas à droite)
    for row in range(3):
        for col in range(4):
            pieces = [board[row+i][col+i] for i in range(4)]
            score += evaluate_pieces(pieces, player)

    # Vérifier les alignements diagonaux (en haut à droite vers le bas à gauche)
    for row in range(3):
        for col in range(3, 7):
            pieces = [board[row+i][col-i] for i in range(4)]
            score += evaluate_pieces(pieces, player)

    return score


def evaluate_pieces(pieces: list[Union[Player, None]], player: Player) -> float:
    if pieces.count(player) == 4:
        return float('+inf')
    elif pieces.count(player) == 3 and pieces.count(None) == 1:
        return 5
    elif pieces.count(player) == 2 and pieces.count(None) == 2:
        return 2
    else:
        return 0
