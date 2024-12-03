import re
from re import findall

file_path = 'Input3.txt'

# Define the regex pattern
pattern = r'mul\(\d{1,3},\d{1,3}\)'
pattern_number = r'\d{1,3}'
pattern2 = r'^do\(\)(?:(?!do\(\)|dont\(\)|mul\(\d{1,3},\d{1,3}\)).)*mul\(\d{1,3},\d{1,3}\)$'
pattern3 = r'^(?:(?!do\(\)|dont\(\)|mul\(\d{1,3},\d{1,3}\)).)*mul\(\d{1,3},\d{1,3}\)$'
pattern_do = r'do\(\)'
pattern_dont = r'don\'t\(\)'


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
        for line in file:
            line_matches = re.findall(pattern, line)
            matches.extend(line_matches)

    print(len(matches))
    for match in matches:
        num = re.findall(pattern_number, match)
        numbers.extend(num)
        result += (int(num[len(num)-2]) * int(num[len(num)-1]))
        num.clear()
    return result

def parse_text_file(input):
    extracted_sections = []
    current_section = []

    with open(file_path, 'r') as file:
        for line in file:
            pattern = re.compile(input)
            # Check if the line matches the regex pattern
            if pattern.search(line):
                # If there's already a section in progress, save it
                if current_section:
                    extracted_sections.append("".join(current_section))
                # Start a new section
                current_section = [line]
            else:
                # Add line to the current section if it exists
                if current_section:
                    current_section.append(line)

        # Add the last section if it wasn't already saved
        if current_section:
            extracted_sections.append("".join(current_section))

    return extracted_sections

print(parse_text_file(pattern))