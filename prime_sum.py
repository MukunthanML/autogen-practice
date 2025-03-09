# filename: prime_sum.py

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(n):
    """Calculate the sum of the first 'n' prime numbers."""
    prime_sum = 0
    prime_count = 0
    num = 2
    while prime_count < n:
        if is_prime(num):
            prime_sum += num
            prime_count += 1
        num += 1
    return prime_sum

# Calculate the sum of 10 prime numbers
prime_sum = sum_of_primes(10)
print("The sum of the first 10 prime numbers is:", prime_sum)