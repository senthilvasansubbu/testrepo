import copy

original = [[1, 2], [3, 4,], [5, 6]]

# Shallow copy creates a new outer container but retains references to nested objects.
shallowcopy = copy.copy(original)

# Deep copy recursively copies nested objects.
deepcopy = copy.deepcopy(original)

print(shallowcopy)
print(deepcopy)

print(f"shallow_copy: {shallowcopy}")
print(f"deep_copy: {deepcopy}")