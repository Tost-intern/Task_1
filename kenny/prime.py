num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("The number is NOT a prime number.")
            break
    else:
        print("The number is a prime number.")
else:
    print("The number is NOT a prime number.")