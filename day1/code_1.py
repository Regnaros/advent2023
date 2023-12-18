import re

pattern = re.compile(r'(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))')

def find_all_numbers(input_string):
    return pattern.findall(input_string)

file_path = "input.txt"

result = 0

def word_to_number(word):
    word_to_number_mapping = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    return word_to_number_mapping.get(word.lower(), None)

def check_for_type(input):
    if input.isdigit():
        return input
    else:
        return word_to_number(input)

with open(file_path, 'r') as file:
    for line in file:
        number_list = find_all_numbers(line)
        result_str = check_for_type(number_list[0]) + check_for_type(number_list[-1])
        
        if result_str.isdigit():
            integer_value = int(result_str)
            result += integer_value

print(result)