# for can check everything
from collections import Iterable
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

for key in L:
    print(key)

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key, d[key])

for k, v in d.items():
    print(k, v)


# use Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(1234, Iterable))

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# enumerate convert a list to dict
for i, v in enumerate(['A', 'B', 'C']):
    print(i, v)

