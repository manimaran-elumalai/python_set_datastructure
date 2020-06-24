sample_set1 = set(range(0, 20, 2))
print(sample_set1)
sample_tuple = (2, 6, 10, 17)
sample_set2 = set(sample_tuple)
print(sample_set2)

print(sample_set1.intersection(sample_set2))
print(sample_set1 & sample_set2)
print("**" * 40)

print(sample_set2.intersection(sample_set1))
print(sample_set2 & sample_set1)