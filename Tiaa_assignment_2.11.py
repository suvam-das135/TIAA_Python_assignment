def check_divisibility_by_5(binary_numbers):
    divisible_by_5 = [number for number in binary_numbers if int(number, 2) % 5 == 0]
    return divisible_by_5

# Get the input sequence of comma-separated 4-digit binary numbers from the user
input_sequence = input("Enter a sequence of comma-separated 4-digit binary numbers: ").split(',')

# Check divisibility by 5 and print the numbers that are divisible by 5
result = check_divisibility_by_5(input_sequence)

# Print the numbers that are divisible by 5 in a comma-separated sequence
print(','.join(result))
