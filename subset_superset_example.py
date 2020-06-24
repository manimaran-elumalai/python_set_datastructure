sample_set1 = set(range(0, 20, 2))
print(sample_set1)
sample_tuple = (2, 4, 6, 10)
sample_set2 = set(sample_tuple)
print(sample_set2)

if sample_set2.issubset(sample_set1):
    print("sample_set2 is a subset of sample_set1")

print("**" * 10)

if sample_set1.issuperset(sample_set2):
    print("sample_set1 is a superset of sample_set2")