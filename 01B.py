row1 = [int(y) for y in [x.split()[0] for x in open('Inputs/01A.txt').readlines()]]
row2 = [int(y) for y in [x.split()[1] for x in open('Inputs/01A.txt').readlines()]]

mult = [0] * len(row1)

for i,x in enumerate(row1):
    for y in row2:
        if x == y:
            mult[i] += 1

print(sum([a*b for a,b in zip(row1,mult)]))