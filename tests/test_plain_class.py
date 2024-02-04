import importlib
from unittest import mock

import pytest

from mock_decorator import MockDecorator
from tests.example import plain_class, plain_func


@pytest.fixture(autouse=True)
def _reset():
    plain_class.logger.reset_mock()
    yield
    importlib.reload(plain_class)
    importlib.reload(plain_func)


def test_simple_decorator_class_with_args():
    importlib.reload(plain_func)
    assert plain_class.logger.call_count == 2

    assert plain_func.ClassWithArgs("Value1", "Value2").value == "ClassWithArgs: done"
    assert plain_class.logger.call_count == 5
    plain_class.logger.assert_has_calls(
        [
            mock.call("creating decorator", "decorator_plain_or_with_args", "arg1", "arg2"),
            mock.call("wrapping class", "decorator_plain_or_with_args"),
            mock.call("before wrapped class", "decorator_plain_or_with_args"),
            mock.call("doing something", "ClassWithArgs", "Value1", "Value2"),
            mock.call("after wrapped class", "decorator_plain_or_with_args"),
        ]
    )


def test_introspection():
    assert plain_func.ClassWithArgs.__name__ == "ClassWithArgs"


def test_mock_decorator():
    with mock.patch.object(
        plain_class, "decorator_plain_or_with_args", MockDecorator()
    ) as decorator_plain_or_with_args:
        importlib.reload(plain_func)

    assert plain_class.logger.call_count == 0

    decorator_plain_or_with_args.ClassWithArgs.assert_called_once_with(arg1="arg1", arg2="arg2")
    assert plain_func.ClassWithArgs("Value1", "Value1").value == "ClassWithArgs: done"


def test_mock_decorator_introspection():
    with mock.patch.object(plain_class, "decorator_plain_or_with_args", MockDecorator()):
        importlib.reload(plain_func)

    assert plain_func.ClassWithArgs.__name__ == "ClassWithArgs"
