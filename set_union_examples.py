sample_set1 = set(range(0, 20, 2))
print(sample_set1)
sample_tuple = (2, 6, 10, 17)
sample_set2 = set(sample_tuple)
print(sample_set2)

print(sample_set2.union(sample_set1))
print(sample_set1.union(sample_set2))