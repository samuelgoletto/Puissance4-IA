from game.game_manager import *


def main():
    board = Board()
    print(board)

    while not is_game_over(board):
        # tour du joueur
        player_column = player_choose_column(board)
        play_in_column(board, player_column, 1)
        print(board)
        if is_winning_move(board, 1):
            print("Tu as gagné !")
            break
        if board.is_full():
            print("Match nul !")
            break

        # tour de l'IA
        ai_column = ai_choose_column(board)
        play_in_column(board, ai_column, 2)
        print(board)
        if is_winning_move(board, 2):
            print("L'IA a gagné !")
            break
        if board.is_full():
            print("Match nul !")
            break
    print("Fin de la partie !")


if __name__ == '__main__':
    main()
