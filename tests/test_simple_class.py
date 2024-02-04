import importlib
from unittest import mock

import callee
import pytest

from mock_decorator import MockDecorator
from tests.example import simple_class, simple_func


@pytest.fixture(autouse=True)
def _reset():
    simple_class.logger.reset_mock()
    yield
    importlib.reload(simple_class)
    importlib.reload(simple_func)


def test_simple_decorator_simple_class():
    importlib.reload(simple_func)
    assert simple_class.logger.call_count == 1

    assert simple_func.SimpleClass().value == "SimpleClass: done"
    assert simple_class.logger.call_count == 4
    simple_class.logger.assert_has_calls(
        [
            mock.call("wrapping class", "simple_class_decorator"),
            mock.call("before wrapped class", "simple_class_decorator"),
            mock.call("doing something", "SimpleClass"),
            mock.call("after wrapped class", "simple_class_decorator"),
        ]
    )


def test_introspection():
    assert simple_func.SimpleClass.__name__ == "SimpleClass"


def test_mock_decorator():
    with mock.patch.object(simple_class, "simple_class_decorator", MockDecorator()) as simple_class_decorator:
        importlib.reload(simple_func)

    assert simple_class.logger.call_count == 0

    simple_class_decorator.SimpleClass.assert_called_once_with(callee.Callable())
    assert simple_class_decorator.SimpleClass.call_args[0][0].__name__ == "SimpleClass"

    assert simple_func.SimpleClass().value == "SimpleClass: done"


def test_mock_decorator_introspection():
    with mock.patch.object(simple_class, "simple_class_decorator", MockDecorator()):
        importlib.reload(simple_func)

    assert simple_func.SimpleClass.__name__ == "SimpleClass"
