def generate_squared_dict(n):
    squared_dict = {i: i*i for i in range(1, n+1)}
    return squared_dict

# Get the input number from the user
n = int(input("Enter a number: "))

# Generate the squared dictionary
result_dict = generate_squared_dict(n)

# Print the dictionary
print(result_dict)
