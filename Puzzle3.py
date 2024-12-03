import re
file_path = 'Input3.txt'

# Define the regex pattern
pattern = r'mul\(\d{1,3},\d{1,3}\)'
pattern_number = r'\d{1,3}'
pattern2 = r'do\(\).*mul\(\d{1,3},\d{1,3}\)'


matches = []
numbers = []



def task_1():
    # Open the file and read it line by line
    result = 0
    with open(file_path, 'r') as file:
        for line in file:
            line_matches = re.findall(pattern, line)
            print(line_matches)
            matches.extend(line_matches)


    for match in matches:
        num = re.findall(pattern_number, match)
        numbers.extend(num)
        result += (int(num[0]) * int(num[1]))
        num.clear()

    return(result)