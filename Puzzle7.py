filename = 'Input7.txt'
equations_standard = []

with open('Input7.txt', 'r') as file:
    data = file.readlines()

for line in data:
    if ":" in line:
        key, values = line.split(":")
        row = [int(key.strip())] + [int(x) for x in values.split()]
        equations_standard.append(row)


def adding(x, y):
    xInt = int(x)
    yInt = int(y)
    return xInt + yInt


def multiply(x, y):
    xInt = int(x)
    yInt = int(y)
    return xInt * yInt


def concatinate(x, y):
    xInt = str(x)
    yInt = str(y)
    concate = xInt + yInt
    return int(concate)


def equation_correct(row1):
    if len(row1) == 2:
        return row1[0] == row1[1]

    sum_row = [row1[0], adding(row1[1], row1[2])] + row1[3:]
    mul_row = [row1[0], multiply(row1[1], row1[2])] + row1[3:]

    return equation_correct(sum_row), equation_correct(mul_row)


def equation_correct_advanced(row1):
    if len(row1) == 2:
        return row1[0] == row1[1]

    sum_row = [row1[0], adding(row1[1], row1[2])] + row1[3:]
    mul_row = [row1[0], multiply(row1[1], row1[2])] + row1[3:]
    concat_row = [row1[0], concatinate(row1[1], row1[2])] + row1[3:]

    return equation_correct_advanced(sum_row), equation_correct_advanced(mul_row), equation_correct_advanced(concat_row)


def contains_true(nested):
    if isinstance(nested, bool):  # Base case: if it's a single boolean value
        return nested
    return any(contains_true(sub) for sub in nested)


def all_equations(equations):
    sum = 0
    incorrect = []
    for equation in equations:
        result = equation[0]
        if contains_true(equation_correct(equation)):
            sum += result
        else:
            incorrect.append(equation)
    return sum, incorrect


def incorrect_equations(equations):
    sum = 0
    for equation in equations:
        result = equation[0]
        if contains_true(equation_correct_advanced(equation)):
            sum += result
    return sum

result, incorrect = all_equations(equations_standard)
result2 = incorrect_equations(incorrect)
print(result)
print(result2)
print(result + result2)

