def sort_words(input_string):
    words_list = input_string.split(',')
    sorted_words = sorted(words_list)
    return sorted_words

input_sequence = input("Enter a comma-separated sequence of words: ")

result = sort_words(input_sequence)

print(','.join(result))
