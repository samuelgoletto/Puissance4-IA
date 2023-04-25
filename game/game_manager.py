from game.entities import Board, Player


def is_winning_move(board: Board, player: Player) -> bool:
    # Vérifier les alignements horizontaux
    for row in range(6):
        for col in range(4):
            pieces = board[row][col:col+4]
            if pieces.count(player) == 4:
                return True

    # Vérifier les alignements verticaux
    for row in range(3):
        for col in range(7):
            pieces = [board[row+i][col] for i in range(4)]
            if pieces.count(player) == 4:
                return True

    # Vérifier les alignements diagonaux (en haut à gauche vers le bas à droite)
    for row in range(3):
        for col in range(4):
            pieces = [board[row+i][col+i] for i in range(4)]
            if pieces.count(player) == 4:
                return True

    # Vérifier les alignements diagonaux (en haut à droite vers le bas à gauche)
    for row in range(3):
        for col in range(3, 7):
            pieces = [board[row+i][col-i] for i in range(4)]
            if pieces.count(player) == 4:
                return True

    return False
