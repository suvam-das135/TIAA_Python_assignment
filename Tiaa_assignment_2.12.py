def is_all_digits_even(number):
    return all(int(digit) % 2 == 0 for digit in str(number))

def find_even_digit_numbers(start, end):
    even_digit_numbers = [num for num in range(start, end + 1) if is_all_digits_even(num)]
    return even_digit_numbers

# Find even digit numbers between 1000 and 3000
result = find_even_digit_numbers(1000, 3000)

# Print the numbers in a comma-separated sequence
print(','.join(map(str, result)))
