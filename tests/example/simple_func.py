from tests.example import simple_class, simple_dec, simple_fwa


@simple_dec.simple_decorator
def simple_function():
    simple_dec.logger("doing something", "simple_function")
    return "simple_function: done"


@simple_fwa.simple_function_with_args_decorator
def function_with_args(arg1, arg2="default"):
    simple_fwa.logger("doing something", "function_with_args")
    return f"function_with_args: {arg1} {arg2} done"


@simple_class.simple_class_decorator
class SimpleClass:
    def __init__(self):
        simple_class.logger("doing something", "SimpleClass")
        self.value = "SimpleClass: done"
