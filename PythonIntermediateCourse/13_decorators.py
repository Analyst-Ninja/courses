# Types of Decorators in Python
# 1. Function Decorators --> Most Common
# 2. Class Decorators

# Decorator --> Functions that takes another function and extends the behaviour of the function

# Functions in Python are 1st Class Objects --> That means it can be pass as variables

# @mydecorator
# def do_something():
#     pass

# # Example 1:
# import functools

# def start_end_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')
#         return result

#     return wrapper


# # @start_end_decorator
# # def print_name():
# #     print('Rohit')

# # print_name = start_end_decorator(print_name) # --> Similar to write @start_end_decorator
# # # But @start_end_decorator is easy to write and improves readability

# @start_end_decorator
# def add5(x):
#     return x + 5

# print(help(add5))
# print(add5.__name__)

# Example 2:

# import functools

# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat


# @repeat(num_times=3)
# def greet(name):
#     print(f'Hello {name}')

# greet('Rohit')

# Example 3: Stacked Decorator

# import functools

# def start_end_decorator(func):

#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('Start')
#         result = func(*args, **kwargs)
#         print('End')
#         return result
#     return wrapper


# def debug(func):

#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         print(f"Calling {func.__name__} ({signature})")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__!r} retured {result!r}")
#         return result
#     return wrapper


# @debug
# @start_end_decorator
# def say_hello(name):
#     result = f"Hello {name}"
#     return result

# print(say_hello("Rohit\n"))

# Class Decorator


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print(f"Hello")


say_hello()
say_hello()
say_hello()
say_hello()

# Use Cases of Decorator

# 1. To calculate the execution time of the function
# 2. Debug the data/ arguments of the functions
# 3. Check if the arguemnets fulfills some requirements
# 4. Cache the return values
# 5. Add Information and update the State
