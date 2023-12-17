s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(1)

print(s)

s.clear()

print(s)

s = {1, 2, 3}
sc = s.copy()

s.add(4)

print(s)
print(sc)
print(s.difference(sc))

sc = {1, 4, 5}

s.difference_update(sc)

print(s)

s1 = {1, 2, 3}
s2 = {1, 2, 4}
s3 = {5}

print(s1.intersection(s2))
print(s1.intersection_update(s2))
print(s1)

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

print(s1.issubset(s2))
print(s1.issuperset(s2))

print(s1.union(s2))

print(s1.symmetric_difference(s2))
print(s1.symmetric_difference_update(s2))
