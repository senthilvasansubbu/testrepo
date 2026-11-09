# object values can be altered after created, it stores unique elements

numbers = [1, 2, 3, 4, 5, 5]
print(f"list values: {numbers}")
unique_numbers = set(numbers)
#  set returns value as {1,2,3,4,5}
print(f"set stores unique values: {unique_numbers}")

# It can be used to check the union, intersection and find the differences

a = {1, 2, 3, 4, 5, 5}
b = {4, 5, 5, 6, 7, 8}

print(f"a union b: {a.union(b)}")
print(f"a intersect b: {a.intersection(b)}")
print(f"a difference b: {a.difference(b)}")
print(f"b difference a: {b.difference(a)}")