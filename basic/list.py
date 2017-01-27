# list 可变的有序集合
classmates = ['Tom','Mike','Bob']
print(classmates)
print(len(classmates))
print(classmates[0])

print(classmates[2])
print(classmates[-1])

classmates.append('Adam')
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

classmates.pop(1)
print(classmates)
# tuple 不可变的无序集合
t = (1, 2, 3, 4, 5)
print(t)
t = ('a', 'b', ['A', 'B'])
t[2][0]='c'
print(t[0][0])