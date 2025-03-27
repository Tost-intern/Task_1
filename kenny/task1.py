name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Print greeting message
print(f"Hello, {name}!")

# Determine age category
if age < 10:
    print("You are a Child.")
elif 10 <= age <= 19:
    print("You are a Teenager.")
else:
    print("You are an Adult.")
