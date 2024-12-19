filename = 'Input7.txt'
equations = []

with open(filename, 'r') as file:
    for line in file:
        equations.append(list(line.strip()))
        parts = line.strip().split(":")
        if len(parts) == 2:
            result = int(parts[0].strip())
            numbers = parts[1].strip().split()
            numbers = [int(num) for num in numbers]
            row = [result] + numbers
            equations.append(row)

sum_row = equations[0] + sum(equations[1], equations[2]) + equations[:,3]
print(sum_row)
def sum (x,y):
    return int(x) + int(y)
def equation_correct(row):
    if len(row) == 2:
        return row[0] == row[1]

    sum_row = row[0] + sum(row[1],row[2]) + row[:,3]



