from collections import defaultdict, deque

updates = []

with open("Inputs/05B.txt", 'r') as b:
    for line in b:
            parts = line.strip().split(',')
            updates.append([int(y) for y in parts])

rules = []

with open("Inputs/05A.txt", 'r') as a:
    for line in a:
            parts = line.strip().split('|')
            rules.append([int(x) for x in parts])

smallest = min(min(inner_list) for inner_list in rules)
biggest = max(max(inner_list) for inner_list in rules)

after = [[] for x in range(biggest - smallest + 1)]

for element in range(smallest, biggest+1):
    for sublist in rules:
        if sublist[0] == element:
            after[element - smallest].append(sublist[1])

def matches_rules(update):
    for x in update:
        new_update = update.copy()
        new_update = new_update[new_update.index(x) + 1:]
        # print(f"For the update {update}, we generate {new_update} and check if it's a subset of {after[x - smallest]}")
        if not set(new_update).issubset(after[x - smallest]):
            return False
    return True

resultA = []
wrongs = []

for gh in updates:
    if matches_rules(gh):
        resultA.append(gh[(len(gh)-1)//2])
    else:
        wrongs.append(gh)

print(f'There are {len(wrongs)} wrong updates and {len(resultA)} correct updates, adding up to {len(wrongs) + len(resultA)} updates, thus matching the total number of {len(updates)} Updates')

print(f'The correct result of Part A is {sum(resultA)}')

# Part A solved here. Correct result is 6505.

def topological_sort(wrong, after, smallest):
    # Create a graph as adjacency list
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Fill the graph with dependencies
    for number in wrong:
        for dependent in after[number - smallest]:
            if dependent in wrong:  # Only consider dependencies within the current wrong list
                graph[number].append(dependent)
                in_degree[dependent] += 1

    # Queue for nodes with no incoming edges
    zero_in_degree_queue = deque([node for node in wrong if in_degree[node] == 0])

    sorted_result = []
    while zero_in_degree_queue:
        node = zero_in_degree_queue.popleft()
        sorted_result.append(node)

        # Decrease the in-degree of each dependent node
        for dep in graph[node]:
            in_degree[dep] -= 1
            # If no more dependencies, add to zero in-degree queue
            if in_degree[dep] == 0:
                zero_in_degree_queue.append(dep)

    # Check if topological sort was possible
    if len(sorted_result) == len(wrong):
        return sorted_result
    else:
        return None  # Sorting not possible satisfying all dependencies


sorted_wrongs = []
for wrong in wrongs:
    sorted_wrong = topological_sort(wrong, after, smallest)
    if sorted_wrong:
        matches = matches_rules(sorted_wrong)
        if matches:
            sorted_wrongs.append(sorted_wrong)

print(f'There are {len(sorted_wrongs)} sorted lists')

resultB = []

for sorted_wrong in sorted_wrongs:
    resultB.append(sorted_wrong[(len(sorted_wrong)-1)//2])

print(f'The correct result of Part B is {sum(resultB)}')

# Part B solved here. Correct result is 6897.