def count_letters_and_digits(input_string):
    letter_count = 0
    digit_count = 0

    for char in input_string:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1

    return letter_count, digit_count

# Get the input sentence from the user
input_sentence = input("Enter a sentence: ")

# Calculate the number of letters and digits
letters, digits = count_letters_and_digits(input_sentence)

# Print the results
print("LETTERS", letters)
print("DIGITS", digits)
