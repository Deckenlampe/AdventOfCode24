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
        row = [int(key.strip())] + [int(x) for x in values.split()]
        equations.append(row)


def adding(x, y):
    xInt = int(x)
    yInt = int(y)
    return xInt + yInt


def multiply(x, y):
    xInt = int(x)
    yInt = int(y)
    return xInt * yInt


def equation_correct(row1):
    if len(row1) == 2:
        return row1[0] == row1[1]

    sum_row = [row1[0], adding(row1[1], row1[2])] + row1[3:]
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
        result = equation[0]
        if contains_true(equation_correct(equation)):
            sum += result
        else:
            incorrect.append(equation)
    return sum, incorrect


def incorrect_equations(equations_incorrect):
    sum = 0

    for equation in equations_incorrect:
        result = equation[0]
        for i in range(1, len(equation) - 1):
            concatinate = str(equation[i]) + str(equation[i + 1])
            row = equation[:i] + [int(concatinate)] + equation[i + 2:]
            if contains_true(equation_correct(row)):
                sum += result

    return sum


def concatinate_row(equation_incorrect):
    concatinated_equation = []
    for i in range(1, len(equation_incorrect) - 1):
        concatinate = str(equation_incorrect[i]) + str(equation_incorrect[i + 1])
        row = equation_incorrect[:i] + [int(concatinate)] + equation_incorrect[i + 2:]
        concatinated_equation.append(row)
    return concatinated_equation

def one_true(equations):
    sum = 0
    for equation in equations:
        result = equation[0]
        if contains_true(equation_correct(equation)):
            sum = result
            break
    return sum

def all_incorrect(equations):
    result = 0
    for equation in equations:
        rows = []
        rows = concatinate_row(equation)
        result += one_true(rows)
    return result


result, incorrect = all_equations(equations)

incorrect_test = []
incorrect_test.append(incorrect[0])
incorrect_test.append(incorrect[1])
incorrect_test.append(incorrect[2])

result2 = (all_incorrect(incorrect))

complete = int(result) + int(result2)
print(complete)
