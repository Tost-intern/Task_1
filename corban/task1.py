
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello, {name}!")

if age < 10:
    print("You are a Child.")
elif 10 <= age <= 19:
    print("You are a Teenager.")
else:
    print("You are an Adult.")
