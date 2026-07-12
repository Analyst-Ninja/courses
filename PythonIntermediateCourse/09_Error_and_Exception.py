# Error and Exception

# --- SyntaxError ---

# a = 5 print(a)

# --- Type Error ---

# a = 5 + '10'

# --- ModuleNotFoundError ---

# import someModuleNotInstalled --> will give ModuleNotFoundError

# --- NameError --- If a value is not defined

# a = c --> c is not defined here

# --- FileNotFoundError ---
# f = open('somefile.txt')

# --- ValueError ---

a = [1, 2, 3]
# a.remove(7)

# --- IndexError ---
# a[100] # Index not present

# --- KeyError ---
a = {"name": "Rohit", "age": 27}

# a['job'] # KeyError

# ---------------------------- Raise Exception ---------------------------

x = -5

# if x < 0:
#     raise Exception('Value Should be Positive')

# assert(x>=0), 'x is not positive'

# try:
#     a = 5/1
#     b = 5 + 10
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('Everything Is Fine')
# finally: # It runs always no matter what
#     print('Cleaning Up...')


# Custom Error Class


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def testValue(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooSmallError("Value is too small", x)


try:
    testValue(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
