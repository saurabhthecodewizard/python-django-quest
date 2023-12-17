l = [1, 2, 3]

print(l)
l.append(4)
print(l)

print(l.count(4))

l.extend([5, 6])
print(l)

print(l.index(2))
l.insert(2, 'inserted')
print(l)
l.pop()
print(l)
l.pop(1)
print(l)
l.remove('inserted')
print(l)
l.reverse()
print(l)