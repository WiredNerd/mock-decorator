import importlib
from unittest import mock

import callee
import pytest

from mock_decorator import MockDecorator
from tests.example import simple_func, simple_fwa


@pytest.fixture(autouse=True)
def _reset():
    simple_fwa.logger.reset_mock()
    yield
    importlib.reload(simple_fwa)
    importlib.reload(simple_func)


def test_simple_decorator_function_with_args():
    importlib.reload(simple_func)
    assert simple_fwa.logger.call_count == 1

    assert simple_func.function_with_args("value1", arg2="value2") == "function_with_args: value1 value2 done"
    assert simple_fwa.logger.call_count == 4
    simple_fwa.logger.assert_has_calls(
        [
            mock.call("wrapping function", "simple_function_with_args_decorator"),
            mock.call("before wrapped function", "simple_function_with_args_decorator"),
            mock.call("doing something", "function_with_args"),
            mock.call("after wrapped function", "simple_function_with_args_decorator"),
        ]
    )


def test_introspection():
    assert simple_func.function_with_args.__name__ == "function_with_args"


def test_mock_decorator():
    with mock.patch.object(
        simple_fwa, "simple_function_with_args_decorator", MockDecorator()
    ) as simple_function_with_args_decorator:
        importlib.reload(simple_func)

    assert simple_fwa.logger.call_count == 0

    simple_function_with_args_decorator.function_with_args.assert_called_once_with(callee.Callable())
    call_args = simple_function_with_args_decorator.function_with_args.call_args
    assert call_args[0][0].__name__ == "function_with_args"

    assert simple_func.function_with_args("value1", arg2="value2") == "function_with_args: value1 value2 done"


def test_mock_decorator_introspection():
    with mock.patch.object(simple_fwa, "simple_function_with_args_decorator", MockDecorator()):
        importlib.reload(simple_func)

    assert simple_func.function_with_args.__name__ == "function_with_args"
