import math

def calculate_Q(input_sequence, C, H):
    result_list = []
    for D in input_sequence:
        Q = int(math.sqrt((2 * C * int(D)) / H))
        result_list.append(Q)
    return result_list

# Fixed values of C and H
C = 50
H = 30


input_sequence = input("Enter a sequence of comma-separated values of D: ").split(',')


result = calculate_Q(input_sequence, C, H)
print(','.join(map(str, result)))
