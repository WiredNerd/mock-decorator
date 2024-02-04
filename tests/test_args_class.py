import importlib
from unittest import mock

import pytest

from mock_decorator import MockDecorator
from tests.example import args_class, args_func


@pytest.fixture(autouse=True)
def _reset():
    args_class.logger.reset_mock()
    yield
    importlib.reload(args_class)
    importlib.reload(args_func)


def test_simple_decorator_class_with_args():
    importlib.reload(args_func)
    assert args_class.logger.call_count == 2

    assert args_func.ClassWithArgs("Value1", "Value2").value == "ClassWithArgs: done"
    assert args_class.logger.call_count == 5
    args_class.logger.assert_has_calls(
        [
            mock.call("creating decorator", "decorator_with_args", "arg1", "arg2"),
            mock.call("wrapping class", "decorator_with_args"),
            mock.call("before wrapped class", "decorator_with_args"),
            mock.call("doing something", "ClassWithArgs", "Value1", "Value2"),
            mock.call("after wrapped class", "decorator_with_args"),
        ]
    )


def test_introspection():
    assert args_func.ClassWithArgs.__name__ == "ClassWithArgs"


def test_mock_decorator():
    with mock.patch.object(args_class, "decorator_with_args", MockDecorator()) as decorator_with_args:
        importlib.reload(args_func)

    assert args_class.logger.call_count == 0

    decorator_with_args.ClassWithArgs.assert_called_once_with("arg1", arg2="arg2")
    assert args_func.ClassWithArgs("Value1", "Value1").value == "ClassWithArgs: done"


def test_mock_decorator_introspection():
    with mock.patch.object(args_class, "decorator_with_args", MockDecorator()):
        importlib.reload(args_func)

    assert args_func.ClassWithArgs.__name__ == "ClassWithArgs"
