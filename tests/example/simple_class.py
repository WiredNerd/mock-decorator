import functools
from unittest import mock

logger = mock.MagicMock()


def simple_class_decorator(cls):
    logger("wrapping class", "simple_class_decorator")

    @functools.wraps(cls)  # corrects introspection
    def wrapper():
        logger("before wrapped class", "simple_class_decorator")
        out = cls()
        logger("after wrapped class", "simple_class_decorator")
        return out

    return wrapper
