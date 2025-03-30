# filename: prime_sum.py

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Only need to check up to the square root
        if n % i == 0:  # If the number is divisible by any number between 2 and its square root, it's not prime
            return False
    return True

def sum_of_primes(n):
    """Calculate the sum of the first 'n' prime numbers."""
    count = 0  # Count of prime numbers found
    num = 2  # Starting number to check for primality
    total_sum = 0  # Sum of prime numbers found
    
    while count < n:  # Continue until we've found 'n' prime numbers
        if is_prime(num):  # Check if the current number is prime
            total_sum += num  # Add it to the sum if it is
            count += 1  # Increment the count of prime numbers found
        num += 1  # Move on to the next number
    
    return total_sum

# Example usage
n = 10  # Calculate the sum of the first 10 prime numbers
result = sum_of_primes(n)
print(f"The sum of the first {n} prime numbers is: {result}")