def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True
    return False

# Loop from 1 to 100 and check for prime numbers
for num in range(1, 101):
    if num > 90:  # Stop at 90
        break
    if is_prime(num):
        print(num, "is prime")

  

  
