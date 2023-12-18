import os

test_path = "test_seeds.txt"
file_path = "input.txt"

total = []

with open(file_path, 'r') as file:
    data = []
    for line in file:
        if "*" in line:
            total.append(data)
            data = []
            continue

        numbers_list = [int(num) for num in line.strip().split()]
        data.append(numbers_list)
    total.append(data)


seeds = total[0][0]

lowest_location = -200

def find_reverse_mapping(number, mapping):
    for r in mapping:
        destination = r[0]
        source = r[1]
        rlenght = r[2]

        if number >= destination and number <= destination + rlenght -1:
            difference = number - destination
            return source + difference
    
    return number

def determine_if_location_exist(number):

    for i in range(0, len(seeds), 2):

        if number >= seeds[i] and number <= seeds[i] + seeds[i+1] -1:
            return True

    return False

for i in range(100000000000000000000):
    current_number = i
    reversed_mapped = i

    for i in range(len(total) -1, 0, -1):
        reversed_mapped = find_reverse_mapping(reversed_mapped, total[i])

    if determine_if_location_exist(reversed_mapped):
        lowest_location = current_number
        break


print(lowest_location)

# Part one
# def find_mapping(number, mapping):
#     for r in mapping:
#         destination = r[0]
#         source = r[1]
#         rlenght = r[2]

#         if number >= source and number <= source + rlenght -1:
#             difference = number - source
#             return destination + difference
        
#     return number

# lowest_location = 9999999999999999999999999999


# for seed in seeds:
#     current_number = seed

#     for i in range(1, len(total), 1):
#         current_number = find_mapping(current_number, total[i])

#     if current_number < lowest_location:
#         lowest_location = current_number