sample_set1 = set(range(0, 20, 2))
print(sample_set1)
sample_tuple = (2, 6, 10, 17, 19, 7, 8)
sample_set2 = set(sample_tuple)
print(sample_set2)

sample_set2.discard(8)
sample_set2.discard(10)

print(sample_set2)
# sample_set2.remove(1) Remove method will return error message if the item member is not in the set) and
# discard method doesn't return any error message
sample_set2.discard(1)

if 1 in sample_set2:
    sample_set2.remove(1)
else:
    print("Item is not the member of the set")

# OR

try:
    sample_set2.remove(1)
except KeyError:
    print("Item 1 is not the member of the set")
