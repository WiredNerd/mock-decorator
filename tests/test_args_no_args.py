import importlib
from unittest import mock

import pytest

from mock_decorator import MockDecorator
from tests.example import args_dec, args_no_args


@pytest.fixture(autouse=True)
def _reset():
    args_dec.logger.reset_mock()
    yield
    importlib.reload(args_dec)
    importlib.reload(args_no_args)


def test_decorator_with_args_function_with_args():
    importlib.reload(args_no_args)
    assert args_dec.logger.call_count == 2

    assert args_no_args.function_with_args("value1", arg2="value2") == "function_with_args: value1 value2 done"
    assert args_dec.logger.call_count == 5
    args_dec.logger.assert_has_calls(
        [
            mock.call("creating decorator", "decorator_with_args", None, None),
            mock.call("wrapping function", "decorator_with_args"),
            mock.call("before wrapped function", "decorator_with_args"),
            mock.call("doing something", "function_with_args"),
            mock.call("after wrapped function", "decorator_with_args"),
        ]
    )


def test_introspection():
    assert args_no_args.function_with_args.__name__ == "function_with_args"


def test_mock_decorator():
    with mock.patch.object(args_dec, "decorator_with_args", MockDecorator()) as decorator_with_args:
        importlib.reload(args_no_args)

    assert args_dec.logger.call_count == 0

    decorator_with_args.function_with_args.assert_called_once_with()
    assert args_no_args.function_with_args("value1", arg2="value2") == "function_with_args: value1 value2 done"


def test_mock_decorator_introspection():
    with mock.patch.object(args_dec, "decorator_with_args", MockDecorator()):
        importlib.reload(args_no_args)

    assert args_no_args.function_with_args.__name__ == "function_with_args"
