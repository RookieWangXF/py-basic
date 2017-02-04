from functools import reduce


def f(x):
    return x * x


def add(x, y):
    return x+y


def fn(x, y):
    return x * 10 + y

r = map(f, [1, 2, 3, 4, 5])

print(list(r))

print(reduce(fn, [1, 2, 3, 4, 5]))

