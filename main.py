from gameManager import *
from AI import *

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