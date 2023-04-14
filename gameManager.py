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