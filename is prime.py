import random

def is_prime(n, k=10):
    """
    Miller-Rabin primality test.
    n: The number to check for primality.
    k: Number of iterations to improve accuracy.
    Returns True if n is likely a prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True  # 2 and 3 are prime
    if n % 2 == 0:
        return False  # Even numbers > 2 are not prime

    # Write n - 1 as 2^r * d with d odd
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Test k times
    for _ in range(k):
        a = random.randint(2, n - 2)  # Pick a random number in [2, n-2]
        x = pow(a, d, n)  # Compute a^d % n
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)  # Square x and take modulo n
            if x == n - 1:
                break
        else:
            return False
    return True

# Test the function
number = int(input("Enter a large number to check if it's prime: "))
if is_prime(number):
    print(f"{number} is a prime number!")
else:
    print(f"{number} is not a prime number.")
