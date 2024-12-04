grid = []

with open("Inputs/04.txt", 'r') as f:
    for line in f:
        line = line.strip()
        grid.append([c for c in line])

n = len(grid[0])
m = len(grid)

def search_word(r, c):
    word = "XMAS"

    if grid[r][c] != word[0]:
        return 0

    # left, right, up, down, lu, ld, ru, rd
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))

    xmas_count = 0
    for r_dir, c_dir in dirs:
        i_word = 1

        new_row, next_col = r + r_dir, c + c_dir

        while i_word < len(word):
            if not (0 <= new_row < m) or not (0 <= next_col < n):
                break

            if grid[new_row][next_col] != word[i_word]:
                break

            i_word += 1
            new_row += r_dir
            next_col += c_dir

        if i_word == len(word):
            xmas_count += 1

    return xmas_count


result = 0
for i in range(0, m):
    for j in range(0, n):
        result += search_word(i, j)
print(result)

# Part A solved. Correct result is 2406.
