def evaluate(board, player):
    score = 0

    # Ajoute du score si le joueur a des jetons sur la colonne du milieu
    center_array = [int(i) for i in list(zip(*board))[3]]
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

def evaluate_pieces(pieces, player):
    if pieces.count(player) == 4:
        return 100
    elif pieces.count(player) == 3 and pieces.count(0) == 1:
        return 5
    elif pieces.count(player) == 2 and pieces.count(0) == 2:
        return 2
    else:
        return 0

def is_winning_move(board, player):
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