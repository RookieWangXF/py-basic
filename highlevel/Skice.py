# 取一个list或tuple的部分元素

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print([L[0], L[1], L[2]])

n = 3
r = []
for i in range(n):
    r.append(L[i])

print(r)
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:-1])

print('ABCDEFG'[:3])