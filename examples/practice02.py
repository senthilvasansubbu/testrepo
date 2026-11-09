#Remove duplicates while preserving order

numbers = [10, 20, 10, 30, 40, 20, 50, 30]
unumber = list(dict.fromkeys(numbers))
print(unumber)

# Python dictionaries preserve insertion order (guaranteed in Python 3.7 and later).

# When you create a dictionary from a sequence:
#- Each list element becomes a dictionary key.
#- Dictionary keys must be unique.
#- The first occurrence establishes the key's insertion position.
#- Subsequent occurrences of the same key do not create additional entries.


def remove_duplicates(numbers):
    return list(dict.fromkeys(numbers))

unique_list = remove_duplicates(numbers)
print(unique_list)