# Set's are unordered and doesn't contain duplicates
# Unlike Dictionary items in sets are not accessed by keys
# In fact, a set is more probably similar to a collection of dictionary keys

sample_set = {1, 3, 5, 6}

for num in sample_set:
    print(num)

sample_set1 = set([4, 2, 0])

for num1 in sample_set1:
    print(num1)

sample_set.add(10)
sample_set1.add(7)
print(sample_set)
print(sample_set1)
sample_set3 = set()
sample_set3.add(15)
print(sample_set3)