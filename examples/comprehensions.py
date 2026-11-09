#traditional approach
numbers = [1, 2, 3, 4, 5, 6]
squares = []

for n in numbers:
    squares.append(n * n)
    print(squares)

print(squares)

print("comprehensions")
#comprehensions approach
squares = [n * n for n in numbers]

print(squares)

print("with filters")
#with filetrs approach
even_numbers = [
    n for n in numbers if n % 2 == 0
]
print(even_numbers)


print("dictionary comphrehension")
#with filetrs approach

squares = {
    n: n * n for n in numbers
}
print(squares)
