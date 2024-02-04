import functools
from unittest import mock

logger = mock.MagicMock()


def decorator_plain_or_with_args(_func=None, *, arg1=None, arg2=None):
    logger("creating decorator", "decorator_plain_or_with_args", arg1, arg2)

    def decorator(func):
        logger("wrapping function", "decorator_plain_or_with_args")

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger("before wrapped function", "decorator_plain_or_with_args")
            out = func(*args, **kwargs)
            logger("after wrapped function", "decorator_plain_or_with_args")
            return out

        return wrapper

    if _func:
        # simple_decorator without arguments
        return decorator(_func)
    return decorator
