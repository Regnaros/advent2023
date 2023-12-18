file_path = "input.txt"
test_path = "test.txt" 

test = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"]

winning_numbers= []
received_numbers= []

with open(file_path, 'r') as file:
    for line in file:
        split_parts = line.split(": ", 1)

        numbers_part = split_parts[1]

            # Split the second part based on "|"
        number_lists = [list(map(int, num_str.split())) for num_str in numbers_part.split(" | ")]

        winning_numbers.append(number_lists[0])
        received_numbers.append(number_lists[1])

def calculate_doubling(n):
    if n == 0:
        return 0

    result = 1
    for _ in range(n - 1):
        result *= 2
        
    return result

copies = { }

for i in range(len(winning_numbers)):
    copies[i] = 1

result = 0

for i in range(0, len(winning_numbers), 1):
    numbers_found = 0

    for number in received_numbers[i]:
        if winning_numbers[i].__contains__(number):
            numbers_found += 1
    
    for j in range(1, numbers_found+1, 1):
        copies[i + j] += copies[i]

for value in copies.values():
    result += value

print(result)

# Part one
# def calculate_doubling(n):
#     if n == 0:
#         return 0

#     result = 1
#     for _ in range(n - 1):
#         result *= 2
        
#     return result

# result = 0

# for i in range(0, len(winning_numbers), 1):
#     numbers_found = 0

#     for number in received_numbers[i]:
#         if winning_numbers[i].__contains__(number):
#             numbers_found += 1

#     result += calculate_doubling(numbers_found)

# print(result)
    
