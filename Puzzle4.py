import re

with open("Input4.txt", "r") as file:
    lines = file.readlines()


pattern = r'XMAS|SAMX'
cnt = 0
horizontal = []
vertical = []
diagonal_arr = []

#horicontally
for line in lines:
    matches = re.findall(pattern, line)
    horizontal.extend(matches)
cnt += len(horizontal)


#vertically
columns = [''.join(line[i] for line in lines) for i in range(len(lines[0]))]
for column in columns:
    matches = re.findall(pattern, column)
    vertical.extend(matches)
cnt += len(vertical)

#diagonally
grid = [list(line) for line in lines]
rows, cols = len(grid), len(grid[0])

# Function to extract all diagonals (top-left to bottom-right)
def get_main_diagonals(grid, rows, cols):
    diagonals = []
    # Top-left to bottom-right diagonals
    for d in range(rows + cols - 1):
        diagonal = []
        for i in range(rows):
            j = d - i
            if 0 <= j < cols:
                diagonal.append(grid[i][j])
        diagonals.append(''.join(diagonal))
    return diagonals

# Function to extract anti-diagonals (top-right to bottom-left)
def get_anti_diagonals(grid, rows, cols):
    diagonals = []
    # Top-right to bottom-left diagonals
    for d in range(rows + cols - 1):
        diagonal = []
        for i in range(rows):
            j = i - d + (cols - 1)
            if 0 <= j < cols:
                diagonal.append(grid[i][j])
        diagonals.append(''.join(diagonal))
    return diagonals

main_diagonals = get_main_diagonals(grid, rows, cols)
anti_diagonals = get_anti_diagonals(grid, rows, cols)
diagonals = main_diagonals + anti_diagonals

for diagonal in diagonals:
    matches = re.findall(pattern, diagonal)
    diagonal_arr.extend(matches)
cnt += len(diagonal_arr)


print(cnt)
