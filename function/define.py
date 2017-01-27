def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-3))

def my_type(y):
    return isinstance(y, int)

print(my_type(12))

import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

r = move(100, 100, 60, math.pi / 6)
print(isinstance(r,tuple))
print(r)

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x

    return s

print(power(5, 2))

def enrall(name, gender):
    print('name:',name)
    print('gender:',gender)

enrall('fei','boy')





