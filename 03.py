import re

def find_pattern(file):
    matches_list = []
    with open(file) as f:
        for line in f:
            matches = re.findall(r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)', line)
            if matches:
                matches_list.append(matches)
    return matches_list

result = []

for x in find_pattern('Inputs/03.txt'):
    for pairs in x:
        result.append(int(pairs[0])*int(pairs[1]))

print(sum(result))

# Solved part A. Correct result is 173517243

def find_specific_mul_patterns(file):
    # Define the regex patterns
    mul_pattern = r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)'
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"

    # Initialize a list to hold the matches and a flag to track context
    matches_list = []
    do_context_active = True  # Assume 'do()' context at the start

    # Split the text into lines for iterative processing
    with open(file) as f:
        for line in f:
            # Split the line into segments between 'do()' and 'don't()'
            sections = re.split(f"({do_pattern}|{dont_pattern})", line)

            for section in sections:
                if re.fullmatch(do_pattern, section):
                    do_context_active = True
                elif re.fullmatch(dont_pattern, section):
                    do_context_active = False
                elif do_context_active:
                    # Find 'mul(a,b)' matches in the current section
                    matches = re.findall(mul_pattern, section)
                    if matches:
                        matches_list.extend(matches)

    return matches_list

resultB = []

for y in find_specific_mul_patterns('Inputs/03.txt'):
        resultB.append(int(y[0])*int(y[1]))

print(sum(resultB))

# Part B solved. Correct result is 100450138