# for loop with range
print("loop:")
for i in range(11):
    print(i)

# while loop
print("while")
count = 1
while count <= (5):
    print (count)
    count += 1

print("break")
# for loop with break
for i in range(11):
    if i == 5:
        break
    print(i)

print("range continue")
# for loop with continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("range pass")
for i in range(1, 6):
    if i == 3:
        pass  # TODO: Handle this case later
    print(i)