#The Fibonacci sequence is a pattern of numbers where each number is the sum of the previous two numbers, usually starting with 0 and 1.
#The user gets to input the amount of Fibonacci numbers to generate


# Generate the first N Fibonacci numbers
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Get number of Fibonacci numbers to generate
num = int(input())

# Generate and print the numbers
for i in range(num):
    print(fibonacci(i))
