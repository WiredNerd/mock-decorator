import importlib
from unittest import mock

import callee
import pytest

from mock_decorator import MockDecorator
from tests.example import simple_dec, simple_func


@pytest.fixture(autouse=True)
def _reset():
    simple_dec.logger.reset_mock()
    yield
    importlib.reload(simple_dec)
    importlib.reload(simple_func)


def test_simple_decorator():
    importlib.reload(simple_func)
    assert simple_dec.logger.call_count == 1

    assert simple_func.simple_function() == "simple_function: done"
    assert simple_dec.logger.call_count == 4
    simple_dec.logger.assert_has_calls(
        [
            mock.call("wrapping function", "simple_decorator"),
            mock.call("before wrapped function", "simple_decorator"),
            mock.call("doing something", "simple_function"),
            mock.call("after wrapped function", "simple_decorator"),
        ]
    )


def test_introspection():
    assert simple_func.simple_function.__name__ == "simple_function"


def test_mock_decorator():
    with mock.patch.object(simple_dec, "simple_decorator", MockDecorator()) as simple_decorator:
        importlib.reload(simple_func)

    assert simple_dec.logger.call_count == 0

    simple_decorator.simple_function.assert_called_once_with(callee.Callable())
    assert simple_decorator.simple_function.call_args[0][0].__name__ == "simple_function"

    assert simple_func.simple_function() == "simple_function: done"


def test_mock_decorator_introspection():
    with mock.patch.object(simple_dec, "simple_decorator", MockDecorator()):
        importlib.reload(simple_func)

    assert simple_func.simple_function.__name__ == "simple_function"
