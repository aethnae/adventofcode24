from itertools import pairwise

numbers = []
unsafe_reports = []
counter = 0
can_become_safe_counter = 0

with open('Inputs/02A.txt', 'r') as fin:
    for line in fin:
        numbers.append([int(i) for i in line.split()])

def is_safe(nums: list[int]):
    if nums == sorted(nums) or nums == sorted(nums, reverse=True):
        if min([abs(y - x) for (x,y) in pairwise(nums)]) > 0 and max([abs(y - x) for (x,y) in pairwise(nums)]) < 4:
            return True

for report in numbers:
    if is_safe(report):
        counter += 1
    elif not is_safe(report):
        unsafe_reports.append(report)

print(f"There are {counter} reports that are safe")

# Part A solved here. Answer is 314

def can_become_safe(unsafe_report: list[int]) -> bool:
    for i in range(len(unsafe_report)):
        temp_report = unsafe_report[:i] + unsafe_report[i + 1:]
        if is_safe(temp_report):
            return True
    return False

for unsafe_reports in unsafe_reports:
    if can_become_safe(unsafe_reports):
        can_become_safe_counter += 1

print(f"There are {can_become_safe_counter} reports that can become safe")
print(f"There are {counter + can_become_safe_counter} that are now safe")

# Part B solved here. Answer is 373