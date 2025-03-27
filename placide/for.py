print("Basic for loop with range")

for i in range(5):
    print(i)
print("For loop with break")

for i in range(5):
    if i == 3:
        break
    print(i)
print("For loop with continue")

for i in range(5):
    if i == 2:
        continue
    print(i)

adj = ["red", "black", "green"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
        