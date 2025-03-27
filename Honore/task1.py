name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}!")

if age < 10:
    print("You are a Child.")
elif 10 <= age <= 18:
    print("You are a Teen.")
else:
    print("You are an Adult.")