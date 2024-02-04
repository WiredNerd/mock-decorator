from tests.example import args_dec


@args_dec.decorator_with_args("call1", arg2="arg2")
@args_dec.decorator_with_args("call2", arg2="arg2")
def function_1():
    args_dec.logger("doing something", "function_1")
    return "function_1: done"


@args_dec.decorator_with_args("call3", arg2="arg2")
def function_2():
    args_dec.logger("doing something", "function_2")
    return "function_2: done"
