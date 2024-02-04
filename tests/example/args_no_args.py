from tests.example import args_class, args_dec


@args_dec.decorator_with_args()
def function_with_args(arg1, arg2="default"):
    args_dec.logger("doing something", "function_with_args")
    return f"function_with_args: {arg1} {arg2} done"


@args_class.decorator_with_args()
class ClassWithArgs:
    def __init__(self, arg1, arg2="default"):
        args_class.logger("doing something", "ClassWithArgs", arg1, arg2)
        self.value = "ClassWithArgs: done"
