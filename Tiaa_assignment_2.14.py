def count_uppercase_and_lowercase(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Get the input sentence from the user
input_sentence = input("Enter a sentence: ")

# Calculate the number of uppercase and lowercase letters
upper_case, lower_case = count_uppercase_and_lowercase(input_sentence)

# Print the results
print("UPPER CASE", upper_case)
print("LOWER CASE", lower_case)
