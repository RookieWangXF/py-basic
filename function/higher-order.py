# function naturally is a var


def add(x, y, f):
    return f(x) + f(y)

print(abs(-30))

print(add(-3, 2, abs))



