def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Loop from 1 to 100 and print prime numbers, stopping at 90
for i in range(1, 101):
    if i == 90:  # Corrected condition (num → i)
        break
    if is_prime(i):
        print(i)
