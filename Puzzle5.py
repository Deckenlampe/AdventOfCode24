import math

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

rules, pattern = task_1()

correct = True
cnt = 0
index = 0
def correct_pattern():
    incorrect = []
    cnt = 0
    for i in range(len(pattern)):
        correct = True
        for j in range(len(pattern[i])):
            for k in range(len(pattern[i])):
                for rule in rules:
                    if rule[0] == pattern[i][k] and rule[1] == pattern[i][j] and k > j:
                        correct = False
                        incorrect.append(pattern[i])
                        break
                if not correct:
                    break
            if not correct:
                break
        if correct:
            index = math.ceil((len(pattern[i])) / 2) - 1
            cnt += (pattern[i][index])
    return(cnt, incorrect)

cnt, incorrect = correct_pattern()

print(incorrect)

def incorrect_pattern():
    for i in range(len(incorrect)):
        for j in range(len(incorrect[i])):
            for k in range(len(pattern[i])):
                for rule in rules:
                    # von vorne nach HInten aufbauen oder von hinten nach Vorne?