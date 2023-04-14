def format_board(content):
    # transforme la chaine de 42 caractères en un tableau à 2 dimensions de 6 lignes et 7 colonnes
    # chaque sous-chaine de 6 caractères correspond à une lign
    board = []
    for i in range(6):
        column = []
        for j in range(7):
            column.append(content[5-i+j*6])
        board.append(column)
    # remplace tous les h par des 1 et les m par des 2
    for i in range(6):
        for j in range(7):
            if board[i][j] == 'h':
                board[i][j] = 1
            elif board[i][j] == 'm':
                board[i][j] = 2
            else:
                board[i][j] = 0
    return board

def print_board(board):
    # affiche le tableau
    for i in range(6):
        for j in range(7):
            print(board[i][j], end=' ')
        print()

def evaluate(board, player):
    score = 0

    # Ajoute du score si le joueur a des jetons sur la colonne du milieu
    center_array = [int(i) for i in list(zip(*board))[3]]
    center_count = center_array.count(player)
    #score += center_count * 3
    
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


    
if __name__ == '__main__':
    # lecture du fichier
    with open('input.txt', 'r') as f:
        content = f.read()
    # formatage du tableau à partir de la chaine de caractères
    board = format_board(content)
    # affichage du tableau
    print_board(board)
    print("Score du joueur 1 : ",evaluate(board, 1))
    print("Score du joueur 2 : ",evaluate(board, 2))