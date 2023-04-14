from AI import *
import random

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

def create_board():
    # crée un tableau vide
    board = []
    for i in range(6):
        column = []
        for j in range(7):
            column.append(0)
        board.append(column)
    return board

def is_board_full(board):
    for row in range(6):
        for col in range(7):
            if board[row][col] == 0:
                return False
    return True

def is_game_over(board):
    return is_winning_move(board, 1) or is_winning_move(board, 2) or is_board_full(board)

def can_play_in_column(board, col):
    return board[0][col] == 0

def play_in_column(board, col, player):
    # joue dans la colonne choisie
    for i in range(5, -1, -1):
        if board[i][col] == 0:
            board[i][col] = player
            break
    return board

def player_choose_column(board):
    print("A toi de jouer !")
    while True:
        choice = input("Choisis une colonne (1-7) : ")
        # si ce n'est pas un chiffre entre 1 et 7, on recommence
        if not choice.isdigit() or int(choice) < 1 or int(choice) > 7:
            print("Cette colonne n'existe pas !")
            continue
        choice = int(choice)-1
        # si la colonne est pleine, on recommence
        if not can_play_in_column(board, int(choice)):
            print("Cette colonne est pleine !")
            continue
        break
    # on renvoie la colonne choisie
    return choice

def ai_choose_column(board):
    print("Au tour de l'IA...")
    while True:
        choice = random.randint(0, 6)
        # si la colonne est pleine, on recommence
        if not can_play_in_column(board, int(choice)):
            continue
        break
    # on renvoie la colonne choisie
    return choice