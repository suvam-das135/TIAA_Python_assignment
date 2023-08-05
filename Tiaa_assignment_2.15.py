def compute_value_of_expression(a):
    result = int(a) + int(a*2) + int(a*3) + int(a*4)
    return result

# Get the input digit from the user
a = input("Enter a digit: ")

# Compute the value of a+aa+aaa+aaaa
output_value = compute_value_of_expression(a)

# Print the result
print(output_value)
