[![Homepage](https://img.shields.io/badge/Homepage-github-white?logo=github)](https://github.com/WiredNerd/mock-decorator)
[![python 3.9 - 3.12](https://img.shields.io/badge/python-3.8%20to%203.12-orange?logo=python&logoColor=green)](https://pypi.org/project/mock-decorator)
[![PyPI - Version](https://img.shields.io/pypi/v/mock-decorator?logo=pypi&logoColor=white)](https://pypi.org/project/mock-decorator)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/mock-decorator)](https://pypistats.org/packages/mock-decorator)
[![PyPI - License](https://img.shields.io/pypi/l/mock-decorator)](https://github.com/WiredNerd/mock-decorator/blob/main/LICENSE)

[![Code Coverage](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FWiredNerd%2Fmock-decorator%2Fmain%2Fcode-coverage.json&query=%24.totals.percent_covered_display&suffix=%25&label=Code%20Coverage&color=teal&logo=pytest&logoColor=green)](https://pytest-cov.readthedocs.io)
[![Mutation Coverage](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FWiredNerd%2Fmock-decorator%2Fmain%2Fmutation-testing-report.json&query=%24.summary.coverage_display&logo=data%3Aimage%2Fsvg%2Bxml%3Bbase64%2CPHN2ZyB3aWR0aD0iMTYuOTMzbW0iIGhlaWdodD0iMTMuNTNtbSIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgMTYuOTMzIDEzLjUzIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxnIHN0cm9rZT0iIzAwMCIgc3Ryb2tlLXdpZHRoPSIxLjEyODYiPjxwYXRoIGQ9Im0zLjEwMDIgMTIuODA0Yy0xLjA2NjItMC41NzEzOC0xLjk3MzUtMS41MTctMi4yMjgyLTIuNzI5OC0wLjM3ODA3LTEuNTU4OS0wLjM1MTE1LTMuMTk0MS0wLjE0NDc0LTQuNzc1IDAuMjE3OTQtMS4zODUgMS4zNjQzLTIuMzQ1NCAyLjQxMjQtMy4xNTI3IDAuOTk3NzQtMC42NzIwMSAyLjEwMzMtMS4yNjM1IDMuMjg3Ny0xLjQ5OTUgMS40MjY3LTAuMTcxNTcgMy4xMzQ0LTAuMTY3ODcgNC4xNTg5IDEuMDA4NiAwLjQ5OTQxIDAuNTI4NTEgMC42OTI5NiAxLjI1NzkgMC42MjI4NSAxLjk2OS0wLjAwNDkgMC44OTcxNCAwLjMwMzkzIDEuOTA3OCAxLjE4IDIuMzE0MyAxLjE0MzkgMC42NTU2OCAyLjUzMDggMC41NTMxMSAzLjcyMTQgMS4wODA4IDAuNzE1OTQgMC43MzgzMi0wLjI1NTQ2IDEuNjMzOC0wLjUxMDYxIDIuMzY1LTAuMzM5MDEgMC45MzMyLTEuMjkzOCAxLjIzNzYtMi4xMzMxIDEuNTQ5Ni0xLjYzNDggMC42NDgzNC0zLjExNTkgMC45NjU3NS01LjIwNTcgMS40MTAzLTIuNzcxMyAwLjcwMjA4LTMuODU0MSAwLjc0ODExLTUuMTYwOSAwLjQ1OTI3eiIgZmlsbD0iIzM3NzZiNSIvPjxwYXRoIGQ9Im0xNS4wMTcgOS40ODYyYy0wLjY4NjM5IDAuMDcyMzA4LTEuNDAxNS0xLjIzNjQtMS4zNDc4LTEuOTc4NSAwLjIwODIxLTAuOTk3NDcgMC44NDk1NS0wLjI1MTkzIDEuMTI1NC0wLjM5OTQgMC4yNTMzNC0wLjEzNDMxIDAuNTEyMTYtMC4xNjYzMSAwLjc3ODk2LTAuMDQ5MzI0IDAuNjA1NzMgMC4zMzk2OCAwLjExNDY0IDEuMjg2Ny0wLjEzNzY2IDEuNzUzOHoiLz48ZWxsaXBzZSBjeD0iOS4zMDM2IiBjeT0iNi4zOTUiIHJ4PSIxLjM0ODEiIHJ5PSIuODA0MDEiLz48L2c+PHBhdGggZD0ibTQuNzc3OSA0LjA3YzAuNjk1ODggMC4zMDQzMiAwLjYwODk5IDAuMzQwMjYgMC41OTUyNiAwLjkxMjk2LTAuMDExNTI1IDEuNjg0MiAwLjY0ODUyIDMuMzU1OCAwLjYwMzg5IDUuMTAxMiAwLjAxNTY2MyAwLjc1NjMzLTAuMDY2MTc3IDAuODQ3NzMtMC4zOTg5NiAxLjc2NDYtMC43NDMyNiAwLjM0MjAyLTEuNDQwOCAwLjE1ODY0LTIuMjc4LTAuMDA1MzM4LTAuODczNDgtMC42MTc4NC0xLjAxODktMC43NTkzMi0xLjQxODQtMi4wMDYzLTAuMzI0MjUtMS44NjQzLTAuMzIwMzYtMy4yOTM3LTAuMDgyODQ2LTQuOTU5NiAwLjE4OTYxLTAuOTY0NTEgMi42MjMyLTAuOTYxNzQgMi45Nzg5LTAuODA3NTYiIGZpbGw9IiMzNzNjNDMiIHN0cm9rZT0iIzM3M2M0MyIgc3Ryb2tlLXdpZHRoPSIxLjEyODYiLz48L3N2Zz4=&label=Mutation%20Coverage&color=3776b5)](https://github.com/WiredNerd/mock-decorator)

[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Code Style: black](https://img.shields.io/badge/Code_Style-Black-black?logo=python&logoColor=black)](https://black.readthedocs.io)
[![Linter: ruff](https://img.shields.io/badge/Linter-Ruff-purple?logo=Ruff)](https://beta.ruff.rs/docs/)
[![Snyk Security](https://img.shields.io/badge/Security-Snyk-939?logo=snyk)](https://snyk.io/)

# Mock Decorator

Mock Decorator simplifes the process of creating a mock for a decorator.

## Features

* Can Mock Function Decorators.
* Can Mock Class Decorators.
* Can Mock Nested Decorators.
* Can Mock Simple Decorators. - like `@my_decorator`
* Can Mock Decorators with arguments. - like `@my_decorator(1)`
* Allows you to verify which Class or Function is decorated.
* Allows you to verify arguments passed to the decorator.

## Why Use Mock Decorator?

Mocking a decorator in python is more difficult than mocking other objects.  The trick is that part of the decorator code is executed at load time, and part is executed when the target function is called.  [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/) is the best article I've found explaining how decorators work.

When possible, it's best to validate the presence of a decorator by validating the effect(s) of the decorator.  But sometimes a mock is required.  

To mock a decorator, the decorator definition must be replaced with a mock before the decorated function is loaded.  [How to mock a decorator in Python](https://dev.to/stack-labs/how-to-mock-a-decorator-in-python-55jc) explains a method for creating a mock for a decorator.  There are also many examples in Stack Overflow.  But I find it very tedious to create a decorator mock.  And tricky to figure out which method was decorated, and what arguments were passed to the decorator.

Mock Decorator is an implementation of a general purpose decorator mock.  It tracks which function(s) were decorated, and which arguments were passed to the decorator.

## Installation

```
pip install mock-decorator --upgrade
```

## Usage

__Note:__ The decorator to be mocked, and the function or class being decorated must be located in different modules.

### Example Usage:

my_functions.py
```python3
from my_decorators import decorator_with_args

@my_dec(1,2)
def my_func(arg1, arg2="default"):
    return f"my_func: {arg1} {arg2} done"
```

test_my_functions.py
```python3
from mock_decorator import MockDecorator
import my_decorators, my_functions
from unittest import mock

def test_my_func():
    with mock.patch.object(my_decorators, "my_dec", MockDecorator()) as mock_dec:  # 1
        importlib.reload(my_functions)                                             # 2
    mock_dec.my_func.assert_called_once_with(1,2)                                  # 3
```

1. Replace the decorator in its module with an instance of MockDecorator.

   Template using mock from unitest: 

   ```python3
   with mock.patch.object(<decorator module>, "<decorator name>", MockDecorator()) as <mock_name>:
   ```

2. Import or Reload the module that includes the decorated function.

   During the loading of the module, the MockDecorator is called to create the decorator wrapper function.  At this time, the MockDecorator will add a MagicMock attribute to itself with the name of the target function.  It will then call the new attribute with the arguments passed to the decorator.

3. Validate the mocked decorator was called with expected arguments.

    Template: `<mock_name>.<decorated function name>.assert_called_once_with(<decorator args>)`

## Contribute

- Issue Tracker: https://github.com/WiredNerd/mock-decorator/issues
- Source Code: https://github.com/WiredNerd/mock-decorator

## Support

If you are having issues, please let us know.

I can be contacted at: pbuschmail-github@yahoo.com

Or by opening an issue: https://github.com/WiredNerd/mock-decorator/issues

## License

The project is licensed under the MIT license.
