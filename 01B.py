# Read the first and second integers from each line in the file and store them in separate lists.
row1 = [int(y) for y in [x.split()[0] for x in open('Inputs/01.txt').readlines()]]
row2 = [int(y) for y in [x.split()[1] for x in open('Inputs/01.txt').readlines()]]

# Initialize a list for keeping track of counts with the same length as row1
mult = [0] * len(row1)

# For each integer in row1, count occurrences in row2
for i, x in enumerate(row1):
    for y in row2:
        if x == y:
            mult[i] += 1

# Calculate the weighted sum and print the result
result = sum([a * b for a, b in zip(row1, mult)])

print(result)