def generate_2d_array(X, Y):
    array_2d = [[i * j for j in range(Y)] for i in range(X)]
    return array_2d

# Get the input
X, Y = map(int, input("Enter two digits X and Y separated by a comma: ").split(','))

result_array = generate_2d_array(X, Y)

for row in result_array:
    print(row)
