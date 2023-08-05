def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Get the input number from the user
num = int(input("Enter a number: "))

# Calculate the factorial
result = factorial(num)

# Print the result
print(result)
