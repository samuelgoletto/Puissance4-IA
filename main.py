from gameManager import *
from AI import *

def main():
    board = create_board()

    while not is_game_over(board):
        # tour du joueur
        column = player_choose_column(board)
        play_in_column(board, column, 1)
        print_board(board)
        if is_winning_move(board, 1):
            print("Tu as gagné !")
            break
        if is_board_full(board):
            print("Match nul !")
            break
        # tour de l'IA


if __name__ == '__main__':
    main()