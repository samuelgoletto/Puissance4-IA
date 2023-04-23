from entities import Board, Player

#
# def is_game_over(board: Board, players: iter) -> bool:
#     return board.is_full() or any(map(lambda p: is_winning_move(board, p), players))


def player_choose_column(board: Board) -> int:
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
