names=['Mike', 'Tom', 'Tracy']
scores = [96, 76, 82]

d = {'Mike': 96, 'Tom': 76, 'Tracy': 82}

print(d['Mike'])

print(d.get('Mike'))

d.pop('Mike')
print(d)

s = set([1, 2, 3, 4, 4])
print(s)
s.add(6)
print(s)
s.remove(2)
print(s)