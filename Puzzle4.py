import re
file_name = "Input4.txt"

map_array = []
with open(file_name, 'r') as file:
    for line in file:
        map_array.append(list(line.strip()))

def xmas_search():

    with open("Input4.txt", "r") as file:
        lines = file.readlines()

    pattern = r'XMAS'
    pattern2 = r'SAMX'

    cnt = 0
    horizontal = []
    vertical = []
    diagonal_arr = []

    #horicontally
    for line in lines:
        print(len(line))
        matches = re.findall(pattern, line)
        horizontal.extend(matches)
        matches = re.findall(pattern2, line)
        horizontal.extend(matches)
    cnt += len(horizontal)


    #vertically
    columns = [''.join(line[i] for line in lines) for i in range(len(lines[0]))]
    for column in columns:
        matches = re.findall(pattern, column)
        vertical.extend(matches)
        matches = re.findall(pattern2, column)
        vertical.extend(matches)
    cnt += len(vertical)

    #diagonally
    grid = [list(line) for line in lines]
    rows, cols = len(grid), len(grid[0])

    main_diagonals = get_main_diagonals(grid, rows, cols)
    anti_diagonals = get_anti_diagonals(grid, rows, cols)
    diagonals = main_diagonals + anti_diagonals

    for diagonal in diagonals:
        matches = re.findall(pattern, diagonal)
        diagonal_arr.extend(matches)
        matches = re.findall(pattern2, diagonal)
        diagonal_arr.extend(matches)

    cnt += len(diagonal_arr)
    return cnt

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

def task_2():
    # Specify the number of characters per row
    chars_per_row = 141
    with open(file_name, 'r') as file:
        text = file.read().strip()
    print(len(text))
    array_2d = [list(text[i:i + chars_per_row]) for i in range(0, len(text), chars_per_row)]
    cnt = 0
    n = 0
    i = 0

    while i < (len(array_2d) - 2):
        while n < (len(array_2d[i]) - 2):
            if array_2d[i][n] == "M":
                if array_2d[i][n + 2] == "S" and array_2d[i + 1][n + 1] == "A" and array_2d[i + 2][n] == "M" and \
                        array_2d[i + 2][n + 2] == "S":
                    cnt += 1
                elif array_2d[i][n +2] == "M" and array_2d[i + 1][n + 1] == "A" and array_2d[i + 2][n] == \
                        array_2d[i + 2][n + 2] == "S":
                    #print(array_2d[i][n + 2], array_2d[i + 1][n + 1], array_2d[i + 2][n], array_2d[i + 2][n + 2])
                    cnt += 1
            elif array_2d[i][n] == "S":
                if array_2d[i][n + 2] == "S" and array_2d[i + 1][n + 1] == "A" and array_2d[i + 2][n] == "M" == \
                        array_2d[i + 2][n + 2]:
                    cnt += 1
                elif array_2d[i][n +2] == "M" and array_2d[i + 1][n + 1] == "A" and array_2d[i + 2][n] == "M" and \
                        array_2d[i + 2][n + 2] == "S":
                    cnt += 1
            n += 1
        i += 1
    return cnt

def check_letter(x, y, letter, map):
    if x < 0 or x >= len(map):
        return False
    elif y < 0 or y >= len(map[x]):
        return False
    elif letter == map[x][y]:
        return True
    return False

def mas_search(map):
    cnt = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if check_letter(i, j, "A", map):
                """ 
                    M.M
                    .A.
                    S.S
                """
                if check_letter(i - 1, j - 1, "M", map) and check_letter(i - 1, j + 1, "M", map) \
                    and check_letter(i + 1, j - 1, "S", map) and check_letter(i + 1, j + 1, "S", map):
                    cnt += 1
                """
                    S.S
                    .A:
                    M.M
                """
                if check_letter(i - 1, j - 1, "S", map) and check_letter(i - 1, j + 1, "S", map) \
                        and check_letter(i + 1, j - 1, "M", map) and check_letter(i + 1, j + 1, "M", map):
                    cnt += 1
                """
                    S.M
                    .A.
                    S.M
                """
                if check_letter(i - 1, j - 1, "S", map) and check_letter(i - 1, j + 1, "M", map) \
                        and check_letter(i + 1, j - 1, "S", map) and check_letter(i + 1, j + 1, "M", map):
                    cnt += 1
                """
                    M.S
                    .A.
                    M.S
                """
                if check_letter(i - 1, j - 1, "M", map) and check_letter(i - 1, j + 1, "S", map) \
                        and check_letter(i + 1, j - 1, "M", map) and check_letter(i + 1, j + 1, "S", map):
                    cnt += 1
    return cnt

print(mas_search(map_array))