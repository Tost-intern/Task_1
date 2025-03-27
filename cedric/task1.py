
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

print(f"Hello {name}!")

if age < 10:
    print("You are a Child")
elif age >= 10 and age <= 19:
    print("You are a Teenager")
else:
    print("You are an Adult")
