import functools
from unittest import mock

logger = mock.MagicMock()


def simple_decorator(func):
    logger("wrapping function", "simple_decorator")

    @functools.wraps(func)  # corrects introspection
    def wrapper():
        logger("before wrapped function", "simple_decorator")
        out = func()
        logger("after wrapped function", "simple_decorator")
        return out

    return wrapper
