def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in range(1, 91):  # Looping from 1 to 90
    if is_prime(num):
        print(num)
