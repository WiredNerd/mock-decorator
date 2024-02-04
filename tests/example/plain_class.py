import functools
from unittest import mock

logger = mock.MagicMock()


def decorator_plain_or_with_args(_cls=None, *, arg1=None, arg2=None):
    logger("creating decorator", "decorator_plain_or_with_args", arg1, arg2)

    def decorator(cls):
        logger("wrapping class", "decorator_plain_or_with_args")

        @functools.wraps(cls)
        def wrapper(*args, **kwargs):
            logger("before wrapped class", "decorator_plain_or_with_args")
            out = cls(*args, **kwargs)
            logger("after wrapped class", "decorator_plain_or_with_args")
            return out

        return wrapper

    if _cls:
        # simple_decorator without arguments
        return decorator(_cls)
    return decorator
