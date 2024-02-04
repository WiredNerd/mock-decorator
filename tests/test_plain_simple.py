import importlib
from unittest import mock

import callee
import pytest

from mock_decorator import MockDecorator
from tests.example import plain_dec, plain_simple


@pytest.fixture(autouse=True)
def _reset():
    plain_dec.logger.reset_mock()
    yield
    importlib.reload(plain_dec)
    importlib.reload(plain_simple)


def test_decorator_plain_or_with_args_function_with_args():
    importlib.reload(plain_simple)
    assert plain_dec.logger.call_count == 2

    assert plain_simple.function_with_args("value1", arg2="value2") == "function_with_args: value1 value2 done"
    assert plain_dec.logger.call_count == 5
    plain_dec.logger.assert_has_calls(
        [
            mock.call("creating decorator", "decorator_plain_or_with_args", None, None),
            mock.call("wrapping function", "decorator_plain_or_with_args"),
            mock.call("before wrapped function", "decorator_plain_or_with_args"),
            mock.call("doing something", "function_with_args"),
            mock.call("after wrapped function", "decorator_plain_or_with_args"),
        ]
    )


def test_introspection():
    assert plain_simple.function_with_args.__name__ == "function_with_args"


def test_mock_decorator():
    with mock.patch.object(plain_dec, "decorator_plain_or_with_args", MockDecorator()) as decorator_plain_or_with_args:
        importlib.reload(plain_simple)

    assert plain_dec.logger.call_count == 0

    decorator_plain_or_with_args.function_with_args.assert_called_once_with(callee.Callable())
    call_args = decorator_plain_or_with_args.function_with_args.call_args
    assert call_args[0][0].__name__ == "function_with_args"

    assert plain_simple.function_with_args("value1", arg2="value2") == "function_with_args: value1 value2 done"


def test_mock_decorator_introspection():
    with mock.patch.object(plain_dec, "decorator_plain_or_with_args", MockDecorator()):
        importlib.reload(plain_simple)

    assert plain_simple.function_with_args.__name__ == "function_with_args"
