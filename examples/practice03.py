import heapq

numbers = [10, 25, 45, 12, 45, 30, 20]

def second_largest(numbers):
    second_largest = heapq.nlargest(2,numbers)[1]
    return second_largest

def second_largest_distinct(numbers):
    second_largest = heapq.nlargest(2,set(numbers))[1]
    return second_largest


second_number = second_largest(numbers)
second_largest_number = second_largest_distinct(numbers)
print(second_number)
print(second_largest_number)
print(set(numbers))

