#. Write a python program that generates the first n numbers in the Fibonacci sequence
def fibonacci(n):
  if n < 0:
    return None
  elif n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Print the Fibonacci series
for i in range(num_terms):
  print(fibonacci(i), end=" ")
