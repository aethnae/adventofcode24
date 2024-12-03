import operator

row1 = sorted([int(y) for y in [x.split()[0] for x in open('Inputs/01.txt').readlines()]])
row2 = sorted([int(y) for y in [x.split()[1] for x in open('Inputs/01.txt').readlines()]])

distances = [abs(x) for x in list(map(operator.sub, row1, row2))]

print(sum(distances))