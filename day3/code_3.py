file_path = "input.txt"
test_path = "test.txt"

input = []

with open(file_path, 'r') as file:
    for line in file:
        char_list = [*line]
        char_list_without_newline = [char for char in char_list if char != '\n']
        input.append(char_list_without_newline)

def check_for_number(input):
    return input.isdigit()

def convert_to_number(s): 
    new = "" 
 
    for x in s: 
        new += x 

    return int(new)

def check_chars_valid(char_list):
    for char in char_list:
        if char != '.' and not char.isdigit():
            return True
    return False

def check_one_char_valid(char, line_index):
    #print("My char : " + char + " line: " + str(input[line_index]))
    if char != '.' and not char.isdigit():
        return True
    return False

def find_numbers_on_line(line, gear_index):

    found_numbers = []
    at_number = False
    start_of_number = -1

    for i in range(0, len(line), 1):
        if line[i].isdigit() and at_number == False:
            start_of_number = i
            at_number = True

        else:
            if line[i].isdigit() == False and at_number:
                found_number = convert_to_number(line[start_of_number:i])
                
                if (gear_index < start_of_number-1 or gear_index > i) == False:              
                    found_numbers.append(found_number)
                    
                at_number = False
                start_of_number = -1
    
    if at_number:
        found_number = convert_to_number(line[start_of_number:])
                
        if (gear_index < start_of_number-1) == False:
            found_numbers.append(found_number)

    return found_numbers



def validate_gear(line_index, gear_index):
    adjacent_top = False
    adjacent_numbers = []

    # Check top left
    if line_index != 0 and gear_index != 0 and input[line_index-1][gear_index-1].isdigit():
        adjacent_top = True

    #Check above
    if line_index != 0 and input[line_index-1][gear_index].isdigit():
        adjacent_top = True

    # Check top right
    if line_index != 0 and gear_index != len(input[line_index])-1 and input[line_index-1][gear_index+1].isdigit():
        adjacent_top = True

    if adjacent_top:
        adjacent_numbers += find_numbers_on_line(input[line_index-1], gear_index)


    
    adjacent_side = False

    # Check left
    if gear_index != 0 and input[line_index][gear_index-1].isdigit():
        adjacent_side = True
    
    # Check right
    if gear_index != len(input[line_index])-1 and input[line_index][gear_index+1].isdigit():
        adjacent_side = True

    if adjacent_side:
        adjacent_numbers += find_numbers_on_line(input[line_index], gear_index)



    adjacent_bottom = False

    # Check bottom
    if line_index != len(input)-1 and input[line_index+1][gear_index].isdigit():
        adjacent_bottom = True
     
    # Check bottom right
    if line_index != len(input)-1 and gear_index != len(input[line_index])-1 and input[line_index+1][gear_index+1].isdigit():
        adjacent_bottom = True
    
    # Check bottom left
    if line_index != len(input)-1 and gear_index != 0 and input[line_index+1][gear_index-1].isdigit():
        adjacent_bottom = True
    
    if adjacent_bottom:
        adjacent_numbers += find_numbers_on_line(input[line_index+1], gear_index)

    if len(adjacent_numbers) == 2:
        return adjacent_numbers[0] * adjacent_numbers[1]
    else:
        return 0

result = 0

#Part two
for line_index in range(0, len(input), 1):
    for char_index in range(0, len(input[line_index]), 1):

        current = input[line_index][char_index]

        if current=="*":
            result += validate_gear(line_index, char_index)
                
print(result)



#Part one

# def validate_number(line_index, start_index, end_index):
#     #Check above
#     if line_index != 0 and check_chars_valid(input[line_index-1][start_index:end_index]):
#         return True
    
#     # Check bottom
#     if line_index != len(input)-1 and check_chars_valid(input[line_index+1][start_index:end_index]):
#         return True
    
#     # Check left
#     if start_index != 0 and check_one_char_valid(input[line_index][start_index-1], line_index):
#         return True
    
#     # Check right
#     if end_index != len(input[line_index])-1 and check_one_char_valid(input[line_index][end_index], line_index):
#         return True
    
#     # Check top left
#     if line_index != 0 and start_index != 0 and check_one_char_valid(input[line_index-1][start_index-1], line_index):
#         return True
        
#     # Check top right
#     if line_index != 0 and end_index != len(input[line_index])-1 and check_one_char_valid(input[line_index-1][end_index], line_index):
#         return True
    
#     # Check bottom right
#     if line_index != len(input)-1 and end_index != len(input[line_index])-1 and check_one_char_valid(input[line_index+1][end_index], line_index):
#         return True
    
#     # Check bottom left
#     if line_index != len(input)-1 and start_index != 0 and check_one_char_valid(input[line_index+1][start_index-1], line_index):
#         return True
    
#     return False


# for line_index in range(0, len(input), 1):

#     start_of_number = -1
#     determining_number = False

#     for char_index in range(0, len(input[line_index]), 1):

#         current = input[line_index][char_index]

#         if check_for_number(current) and determining_number == False:
#             start_of_number = char_index
#             determining_number = True

#         else:
#             if check_for_number(current) == False and determining_number:
#                 number_slice = input[line_index][start_of_number:char_index]
#                 found_number = convert_to_number(number_slice)

#                 if validate_number(line_index, start_of_number, char_index):
#                     result += found_number

#                 start_of_number = -1
#                 determining_number = False
    
#     if determining_number:
#         number_slice = input[line_index][start_of_number:]
#         found_number = convert_to_number(number_slice)

#         if validate_number(line_index, start_of_number, len(input[line_index])-1):
#             result += found_number

# print(result)