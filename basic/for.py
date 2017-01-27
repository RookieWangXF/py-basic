names = ['Mike', 'Bob', 'Tom']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x

print(sum)

# range不包括11自身
for x in range(11):
    sum = sum + x

print(sum)

num = 99
res = 0;
while num > 0:
    res = res + num
    num = num - 2

print(res)