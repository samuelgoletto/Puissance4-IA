from typing import Union

from game.entities import Board, Player


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


# Chapeau
if __name__ == '__main__':
    board = Board()

    board[5][0] = Player('h')
    board[4][0] = Player('h')
    board[3][0] = Player('h')
    board[2][0] = Player('m')
    board[1][0] = Player('h')
    board[0][0] = Player('h')

    board[5][1] = Player('h')
    board[4][1] = Player('h')
    board[3][1] = Player('m')
    board[2][1] = Player('h')
    board[1][1] = Player('h')
    board[0][1] = Player('h')

    board[5][2] = Player('h')
    board[4][2] = Player('h')
    board[3][2] = Player('h')
    board[2][2] = Player('m')
    board[1][2] = Player('h')
    board[0][2] = Player('h')

    board[5][3] = Player('m')
    board[4][3] = Player('m')
    board[3][3] = Player('m')

    board[5][4] = Player('h')
    board[4][4] = Player('h')

    board[5][5] = Player('h')
    board[4][5] = Player('h')
    board[3][5] = Player('h')

    board[5][6] = Player('h')

    print(evaluate(board, Player('h')))
