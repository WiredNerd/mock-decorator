import functools
from unittest import mock

logger = mock.MagicMock()


def decorator_with_args(arg1=None, arg2=None):
    logger("creating decorator", "decorator_with_args", arg1, arg2)

    def decorator(cls):
        logger("wrapping class", "decorator_with_args")

        @functools.wraps(cls)
        def wrapper_repeat(*args, **kwargs):
            logger("before wrapped class", "decorator_with_args")
            out = cls(*args, **kwargs)
            logger("after wrapped class", "decorator_with_args")
            return out

        return wrapper_repeat

    return decorator
