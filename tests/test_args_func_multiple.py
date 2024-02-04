import importlib
from unittest import mock

import pytest

from mock_decorator import MockDecorator
from tests.example import args_dec, args_func_multiple


@pytest.fixture(autouse=True)
def _reset():
    args_dec.logger.reset_mock()
    yield
    importlib.reload(args_dec)
    importlib.reload(args_func_multiple)


def test_mock_decorator():
    with mock.patch.object(args_dec, "decorator_with_args", MockDecorator()) as decorator_with_args:
        importlib.reload(args_func_multiple)

    decorator_with_args.function_1.assert_has_calls(
        [
            mock.call("call2", arg2="arg2"),
            mock.call("call1", arg2="arg2"),
        ]
    )
    decorator_with_args.function_2.assert_called_once_with("call3", arg2="arg2")
