# positional parameter names before '/' are ignored when passing in kwargs with same name, see 5th example
def setup_config(path, /, user='default', *, readonly, **options):
    config = {
        'path': path,
        'user': user,
        'readonly': readonly,
        'options': options
    }
    return config

setup_config('/etc/app', 'admin', readonly=True, timeout=30, retries=2)
setup_config('/etc/app', readonly=False)
setup_config(path='/etc/app', readonly=True)
setup_config('/etc/app', 'guest', True)
setup_config('/etc/app', user='operator', readonly=False, path='/srv/data')

# For each of the function calls below, determine if it is valid or if it will raise an error.
# If it raises an error, explain the specific reason for the error based on the function's signature.

# practicing explaining closures
def call_tracker(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Call {count} to {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@call_tracker
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")

# 1.  The call_tracker function is called with the greet function as its argument (func).
# 2.  Inside call_tracker, a local variable count is initialized to 0.
# 3.  call_tracker defines and returns the wrapper function. This wrapper function becomes the new greet.
# 4.  The wrapper function forms a closure, capturing the count variable from its enclosing call_tracker scope. This count variable will persist between calls to the new greet function.
# 5.  When greet("Alice") is called, it's actually the wrapper function that executes. It increments the captured count to 1, prints the tracking message, and then calls the original greet function.
# 6.  Subsequent calls to greet execute the same wrapper function, which continues to increment the same closed-over count variable.
# The closure allows the wrapper to maintain state (count) across multiple invocations, which is a common pattern for decorators that need to track information or modify behavior based on previous calls.

# The module is cached after being imported the first time.
import calculator
from calculator import add
import calculator as calc

print('Starting main script execution.')

result1 = calculator.subtract(10, 4)
print(f'Result 1: {result1}')

result2 = add(10, 4)
print(f'Result 2: {result2}')

result3 = calc.add(10, 4)
print(f'Result 3: {result3}')

# What will be the output? Specifically, address how many times the code in calculator.py is executed
# and how the different import statements in main.py make the functions available.