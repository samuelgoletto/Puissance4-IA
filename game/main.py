import game.ai.strategies as strat
from game.entities import Player, Board
from game.game_manager import is_winning_move


def main() -> None:

    players_and_sentences = {
        Player('h', strategy=strat.interactive_strategy): {
            'next': 'À toi de jouer !',
            'win': 'Tu as gagné !'
        },
        Player('m', strategy=strat.minimax_strategy): {
            'next': 'Au tour de l\'IA...',
            'win': 'L\'IA a gagné !'
        }
    }

    board = Board()
    print(board)

    while True:
        for player, msg in players_and_sentences.items():
            print(msg['next'])

            # Moves
            column = player.choose_column_to_play(board)
            board.play_in_column(column, player)
            print(board)

            # Endgame checks
            if is_winning_move(board, player):
                print(msg['win'])
                break
            if board.is_full():
                print('Match nul !')
                break
        else:  # Not endgame
            continue
        print('Fin de la partie !')
        break


if __name__ == '__main__':
    main()
