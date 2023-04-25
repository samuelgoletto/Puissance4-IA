import game.ai.strategies as strat
from game.entities import Player, Board
from game.game_manager import is_winning_move
from game.exceptions import *

from fastapi import FastAPI, HTTPException


app = FastAPI()


@app.get("/")
def ayo() -> str:
    return "Connect 4 game against a light AI"


@app.get("/move")
def move(b: str) -> int:
    # Define players with their strategies so that they are handled and stored during the transaction
    player = Player('h', strategy=strat.interactive_strategy)
    machine = Player('m', strategy=strat.minimax_strategy)

    board = Board(b)

    try:
        board.validate()  # Input error
        validate_ongoing_state(board, player, machine)  # Processing error
    except GameError as exc:
        raise HTTPException(status_code=exc.status, detail=exc.message)

    column = machine.choose_column_to_play(board) + 1  # +1 because it is `range(6)` and we want `range(1, 7)`
    print(column)

    column_unary = int('1'*column)  # The result should never be 0

    return column_unary


def validate_ongoing_state(board, player, machine) -> None:

    if board.is_full():
        raise FinalStateError("The grid is already full")

    if is_winning_move(board, player):
        raise FinalStateError("The player has already won")

    if is_winning_move(board, machine):
        raise FinalStateError("The machine has already won")

