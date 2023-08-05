def square_odd_numbers(input_list):
    odd_numbers_squared = [str(int(num) ** 2) for num in input_list if int(num) % 2 != 0]
    return odd_numbers_squared

# Get the input sequence of comma-separated numbers from the user
input_sequence = input("Enter a sequence of comma-separated numbers: ").split(',')

# Square each odd number using list comprehension
result = square_odd_numbers(input_sequence)

# Print the result
print(','.join(result))
