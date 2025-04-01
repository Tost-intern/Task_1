# Ask for the user's name
name = input("Enter your name: ")

# Ask for the user's age and convert it to an integer
age = int(input("Enter your age: "))

# Print a greeting message
print(f"Hello, {name}!")

# Determine if the user is a child, teenager, or adult
if age < 10:
    print("You are a Child.")
elif 10 <= age <= 19:
    print("You are a Teenager.")
else:
    print("You are an Adult.")
