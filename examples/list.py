# object values can be altered after created

numbers = [10, 20, 30, 30]

print(f"list the values: {numbers}")

numbers.append(40)
numbers.remove(30)

print(f"list values after append and remove: {numbers}")

# Insert 15 at index 1 (the second position)
numbers.insert(1, 15)
numbers.insert(1, 12)

print(f"list the insert values by position: {numbers}")

# Remove 12 at index 1 (the second position)
numbers.pop(1)
print(f"list the removed values by position: {numbers}")

# reverse order
numbers.reverse()
print(f"list the reverse order values: {numbers}")

# sort order
numbers.sort()
print(f"list the insert values: {numbers}")
