import functools
from unittest import mock

logger = mock.MagicMock()


def simple_function_with_args_decorator(func):
    logger("wrapping function", "simple_function_with_args_decorator")

    @functools.wraps(func)  # corrects introspection
    def wrapper(*args, **kwargs):
        logger("before wrapped function", "simple_function_with_args_decorator")
        out = func(*args, **kwargs)
        logger("after wrapped function", "simple_function_with_args_decorator")
        return out

    return wrapper
