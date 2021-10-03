# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=import-error
class UserError(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class UserNotFoundError(UserError):
    pass


class UserAlreadyRegisteredError(UserError):
    pass


class InvalidEmailError(UserError):
    pass


class IncorrectPasswordError(UserError):
    pass
