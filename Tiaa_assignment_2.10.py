def remove_duplicates_and_sort(input_string):
    words_list = input_string.split()
    unique_words = sorted(set(words_list))
    return unique_words

# Get the input sequence of whitespace-separated words from the user
input_sequence = input("Enter a sequence of whitespace-separated words: ")

# Remove duplicates and sort the words
result = remove_duplicates_and_sort(input_sequence)

# Print the sorted words after removing duplicates
print(' '.join(result))
