"""MockDecorator is a simple decorator for mocking functions in tests."""

import functools
import sys
from typing import Any
from unittest import mock

if sys.version_info < (3, 14):
    from typing import Callable  # noqa: UP035
else:
    from collections.abc import Callable


class MockDecorator:
    """MockDecorator is a simple decorator for mocking functions in tests."""

    def __call__(self, *d_args, **d_kwargs) -> Callable:
        """Wrap function or class in decorator."""

        def decorator(f: Callable) -> Callable:
            if not hasattr(self, f.__name__):
                setattr(self, f.__name__, mock.MagicMock())
            getattr(self, f.__name__)(*d_args, **d_kwargs)

            @functools.wraps(f)  # corrects introspection
            def wrapper(*args, **kwargs) -> Any:  # noqa: ANN401
                return f(*args, **kwargs)

            return wrapper

        if d_args and callable(d_args[0]):  # nomut: Number
            # simple_decorator without arguments
            return decorator(d_args[0])  # nomut: Number
        # decorator with arguments
        return decorator
