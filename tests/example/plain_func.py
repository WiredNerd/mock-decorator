from tests.example import plain_class, plain_dec


@plain_dec.decorator_plain_or_with_args(arg1="arg1", arg2="arg2")
def function_with_args(arg1, arg2="default"):
    plain_dec.logger("doing something", "function_with_args")
    return f"function_with_args: {arg1} {arg2} done"


@plain_class.decorator_plain_or_with_args(arg1="arg1", arg2="arg2")
class ClassWithArgs:
    def __init__(self, arg1, arg2="default"):
        plain_class.logger("doing something", "ClassWithArgs", arg1, arg2)
        self.value = "ClassWithArgs: done"
