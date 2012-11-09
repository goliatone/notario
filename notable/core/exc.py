"""Notable core exceptions module."""


class NotableError(Exception):
    """Generic errors."""
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return self.msg


class NotableConfigError(NotableError):
    pass


class NotableRuntimeError(NotableError):
    pass


class NotableArgumentError(NotableError):
    pass
