filename = 'Input7.txt'
equations = []

"""
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
"""

with open('Input7.txt', 'r') as file:
    data = file.readlines()

for line in data:
    if ":" in line:
        key, values = line.split(":")
        # Convert the key and values into integers and form a list
        row = [int(key.strip())] + [int(x) for x in values.split()]
        equations.append(row)


def sum(x,y):
    xInt =  int(x)
    yInt = int(y)
    return xInt + yInt

def multiply(x,y):
    xInt = int(x)
    yInt = int(y)
    return xInt * yInt

def equation_correct(row1):
    if len(row1) == 2:
        return row1[0] == row1[1]

    sum_row = [row1[0], sum(row1[1], row1[2])] + row1[3:]
    mul_row = [row1[0], multiply(row1[1], row1[2])] + row1[3:]

    return equation_correct(sum_row), equation_correct(mul_row)

def contains_true(nested):
    if isinstance(nested, bool):  # Base case: if it's a single boolean value
        return nested
    return any(contains_true(sub) for sub in nested)

def all_equations(equations):
    sum = 0
    incorrect = []
    for equation in equations:
        result =  equation[0]
        if contains_true(equation_correct(equation)):
            sum += result
        else:
            incorrect.append(equation)
    return sum, incorrect

result, incorrect = all_equations(equations)
print(incorrect)