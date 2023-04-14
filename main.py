from gameManager import *
from AI import *

def main():
    board = create_board()

    while not is_game_over(board):
        # tour du joueur
        player_column = player_choose_column(board)
        play_in_column(board, player_column, 1)
        print_board(board)
        if is_winning_move(board, 1):
            print("Tu as gagné !")
            break
        if is_board_full(board):
            print("Match nul !")
            break
        # tour de l'IA
        ai_column = ai_choose_column(board)
        play_in_column(board, ai_column, 2)
        print_board(board)
        if is_winning_move(board, 2):
            print("L'IA a gagné !")
            break
        if is_board_full(board):
            print("Match nul !")
            break
    print("Fin de la partie !")

        
if __name__ == '__main__':
    main()