from functools import reduce

strings = ['robot', 'cat', 'tokyo', 'diner', 'gorilla']

print(reduce(lambda accum, string: accum + string, strings))