def capitalize_lines(input_lines):
    capitalized_lines = [line.upper() for line in input_lines]
    return capitalized_lines

# Get the input sequence of lines from the user
input_sequence = []
print("Enter lines (press Enter after each line, and type 'end' to finish):")
while True:
    line = input()
    if line == "end":
        break
    input_sequence.append(line)

# Capitalize the lines
result = capitalize_lines(input_sequence)

# Print the capitalized lines
for line in result:
    print(line)
