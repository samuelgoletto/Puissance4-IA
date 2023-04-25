
class GameError(Exception):
    status = 500

    def __init__(error, message):
        error.message = message


class FinalStateError(GameError):
    status = 422


class InvalidFormatError(GameError):
    status = 400


class InvalidConfiguration(GameError):
    status = 400

