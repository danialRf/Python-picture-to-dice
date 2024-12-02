import random

# Function to check if a number is prime using Miller-Rabin test
def is_prime(n, k=5):  # k is the number of tests
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d (d is odd)
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform k tests
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # Compute a^d % n
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Function to generate a large prime number
def generate_large_prime(bits=1024):
    while True:
        # Generate a random odd number with the specified number of bits
        candidate = random.getrandbits(bits) | 1
        if is_prime(candidate):
            return candidate

# Generate a large prime number with 1024 bits
print("Generating a large prime number...")
large_prime = generate_large_prime(bits=1024)
print("Large Prime Number:", large_prime)
