def generate_list_and_tuple(input_string):
    number_list = input_string.split(',')
    number_tuple = tuple(number_list)
    return number_list, number_tuple

# Get the input sequence of comma-separated numbers from the user
input_sequence = input("Enter a sequence of comma-separated numbers: ")

# Generate the list and tuple
result_list, result_tuple = generate_list_and_tuple(input_sequence)

# Print the list and tuple
print(result_list)
print(result_tuple)

