# use import, test_threenames.py become an object
# we can use test_threenames.attitude to use it
import test_threenames
print(test_threenames.a)
print(dir(test_threenames))
print(test_threenames.__file__)

# '__builtins__', '__cached__', '__doc__', '__file__'
# '__loader__', '__name__', '__package__', '__spec__'
