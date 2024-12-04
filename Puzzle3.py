import re
from re import findall

file_path = 'Input3.txt'

# Define the regex pattern
pattern = r'mul\(\d{1,3},\d{1,3}\)'
pattern_number = r'\d{1,3}'
pattern2 = r'do\(\)(?:(?!do\(\)|dont\(\)).)*mul\(\d{1,3},\d{1,3}\)'
pattern3 = r'^(?:(?!do\(\)|dont\(\)|mul\(\d{1,3},\d{1,3}\)).)*mul\(\d{1,3},\d{1,3}\)'
pattern_do = r'(do\(\))|(don\'t\(\))'
pattern4 = r'do\(\)(?:(?!do\(\)|dont\(\)|mul\(\d{1,3},\d{1,3}\)).)*mul\(\d{1,3},\d{1,3}\)'


matches = []
numbers = []



def task_1():
    # Open the file and read it line by line
    result = 0
    with open(file_path, 'r') as file:
        for line in file:
            line_matches = re.findall(pattern, line)
            matches.extend(line_matches)

    for match in matches:
        num = re.findall(pattern_number, match)
        numbers.extend(num)
        result += (int(num[0]) * int(num[1]))
        num.clear()

    return result

def task_2():
    result = 0
    with open(file_path, 'r') as file:
        content = file.read()

    First_do = re.search(pattern_do, content)
    if First_do:
        cut_content = content[:First_do.start()]
    first_matches = re.findall(pattern, cut_content)

    for match in first_matches:
        num = re.findall(pattern_number, match)
        numbers.extend(num)
        result += (int(num[0]) * int(num[1]))
        num.clear()

    return result

def task2_2():
    result = 0
    with open(file_path, 'r') as file:
        content = file.read()

    matches = list(re.finditer(pattern_do, content))
    do_parts = []

    if matches:
        for i in range(len(matches) - 1):
            if matches[i].group() == "do()":
                start = matches[i].start()
                end = matches[i + 1].start()
                do_parts.append(content[start:end])

        # Handle the last "do()" call
        if matches[-1].group() == "do()":
            do_parts.append(content[matches[-1].start():])

    for part in do_parts:
        part_matches = re.findall(pattern, part)
        for match in part_matches:
            num = re.findall(pattern_number, match)
            numbers.extend(num)
            result += (int(num[0]) * int(num[1]))
            num.clear()
    return result

final_result = task_2() + task2_2()
print(final_result)



