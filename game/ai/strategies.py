import random

from game.ai.heuristics import evaluate
from game.entities import Board, Player
from game.game_manager import is_winning_move


def random_strategy(board: Board, _player_unused: Player = None) -> int:
    """Random selection strategy"""
    remaining = list(range(7))
    remaining.remove(choice := random.choice(remaining))
    while board.is_column_full(choice) and remaining:  # si la colonne est pleine, on recommence
        remaining.remove(choice := random.choice(remaining))

    return choice  # Choice could be invalid if the board is already full


def interactive_strategy(board: Board, _player_unused: Player = None) -> int:
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


def one_step_further_strategy(board: Board, player: Player) -> int:
    next_move_scores = {}
    for column in range(7):
        next_move_scores[column] = evaluate(board.copy().play_in_column(column, player), player)

    return max(next_move_scores.items(), key=lambda t: t[1])[0]


def minimax(board, alpha, beta, player, depth):
    # print(f"Depth: {depth} Alpha: {alpha} Beta: {beta}")
    assert alpha < beta
    random_column = random_strategy(board, player)

    if depth == 0 or board.is_full():
        return evaluate(board, player), None

    for i in range(7):
        board1 = board.copy()
        board1.play_in_column(i, player)
        if is_winning_move(board1, player):
            return evaluate(board1, player), i

    _max = 43  # du chapeau
    if beta > _max:
        beta = _max
        if alpha >= beta:
            # print("Random strategy empty window")
            return beta, random_column

    best_score = -float('inf')
    best_column = None
    for x in range(7):  # compute the score of all possible next move and keep the best one
        if not board.is_column_full(x):
            board1 = board.copy()
            board1.play_in_column(x, player)  # It's opponent turn in P2 position after current player plays x column.
            next_player = Player("m") if player == Player("h") else Player("h")
            score = -minimax(board1, -beta, -alpha, next_player, depth - 1)[
                0]  # explore opponent's score within [-beta;-alpha] windows:
            # no need to have good precision for score better than beta (opponent's score worse than -beta)
            # no need to check for score worse than alpha (opponent's score worse better than -alpha)
            if score > best_score:
                best_score = score
                best_column = x
            if score >= beta:  # prune the exploration if we find a possible move better than what we were looking for.
                return score, x
            if score > alpha:  # reduce the [alpha;beta] window for next exploration, as we only
                # need to search for a position that is better than the best so far.
                alpha = score

    # print(f"Random strategy score too low, alpha: {alpha}")
    return alpha, best_column


def minimax_strategy(board: Board, player: Player) -> int:
    """Minimax strategy"""
    score, column = minimax(board, -43, 43, player, 2)
    return column
