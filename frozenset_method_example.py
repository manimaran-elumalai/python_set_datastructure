#  These sets are immutable and you cannot add, remove/discard anything to it

sample_set1 = frozenset(range(0, 30, 3))
print(sample_set1)
print(len(sample_set1))

#  sample_set1.add(5) - AttributeError: 'frozenset' object has no attribute 'add'

sample_set2 = {21, 9, 12}
print(sample_set2)
print(len(sample_set2))

sample_set3 = set([9, 12])

print(sample_set1.union(sample_set2)) # creates a new set with elements from both the sets
print(len(sample_set1.union(sample_set2)))
print(sample_set1.intersection(sample_set2)) # creates a new set with common elements of both sets
print(len((sample_set1.intersection(sample_set2))))
print(sample_set1.difference(sample_set2)) # creates a new set with elements in a and not in b
print(len(sample_set1.difference(sample_set2)))
print(sample_set1.symmetric_difference(sample_set2)) # creates a new set with elements in either a or b but not in both
print(len(sample_set1.symmetric_difference(sample_set2)))


if sample_set2.issubset(sample_set1):
    print("it is subset")

if sample_set1.issuperset(sample_set2):
    print("yes it is superset")

print("***" * 10)

string1 = "God is great"
string2 = frozenset("aeiou")
string3 = set(string1).difference(string2)
print(string3)
string4 = sorted(string3)
print(string4)