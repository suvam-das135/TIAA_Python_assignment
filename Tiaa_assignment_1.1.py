n = 50

number_range = set(range(n, 1, -1))

primes_list = []

while number_range:
    prime = number_range.pop()

    primes_list.append(prime)

    number_range.difference_update(set(range(prime * 2, n + 1, prime)))

print(primes_list)