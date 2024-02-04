import functools
from unittest import mock

logger = mock.MagicMock()


def decorator_with_args(arg1=None, arg2=None):
    logger("creating decorator", "decorator_with_args", arg1, arg2)

    def decorator(func):
        logger("wrapping function", "decorator_with_args")

        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            logger("before wrapped function", "decorator_with_args")
            out = func(*args, **kwargs)
            logger("after wrapped function", "decorator_with_args")
            return out

        return wrapper_repeat

    return decorator
