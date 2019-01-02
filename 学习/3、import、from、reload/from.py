# use import, test_threenames.py gives us three vars
# we can use varname to use it
from test_threenames import a, b, c, __file__
print(a, 'and', a, b * 2, c + c, __file__)
