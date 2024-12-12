filename = "Input5.txt"
with open(filename, 'r') as file:
    lines = file.readlines()

def task_1():
    array1 = []
    array2 = []
    blank_line_found = False

    for line in lines:
        if line.strip() == '' and not blank_line_found:  # Check for the first blank line
            blank_line_found = True
            continue  # Skip the blank line itself
        if not blank_line_found:
            array1.append(line.strip())  # Add to the first array until the blank line
        else:
            array2.append(line.strip())  # Add to the second array after the blank line

    # Convert to 2D arrays (lists of lists in Python)
    array1 = [list(map(int, line.split('|'))) for line in array1 if line]  # Convert to integers
    array2 = [list(map(int, line.split(','))) for line in array2 if line]  # Convert to integers
    return array1, array2

array1, array2 = task_1()

correct = True
cnt = 0

for i in range(len(array2)):
    for j in range(len(array2[i])):
        for k in range(len(array2[i])):
            for n in range(len(array1)):
                if array1[n][0] == array2[i][j] and array1[n][1] == array2[i][k]:
                    correct = False
                    break
    if correct:
        cnt += 1

print(cnt)

