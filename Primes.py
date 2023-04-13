# Define a function that checks if a number is prime
def is_prime(n):
  # Check if the number is less than or equal to 1
  if n <= 1:
    return False

  # Check if the number is evenly divisible by any number in the range 2 to n - 1
  for i in range(2, n):
    if n % i == 0:
      return False

  # If the number is not evenly divisible by any number in the range, it is prime
  return True

# Test the function with some values
print(is_prime(1))  # False
print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(4))  # False
print(is_prime(5))  # True
