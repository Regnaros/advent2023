import re
import os 

pattern = re.compile(r'[a-zA-Z0-9]+')

def retriveInformation(input_string):
    return pattern.findall(input_string)

dict = {"Game": 0, "red": 0, "blue":0, "green": 0}

script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

file_path = "input.txt"

result = 0

with open(file_path, 'r') as file:
    for line in file:
        dict = {"Game": 0, "red": 0, "blue":0, "green": 0}
        information = retriveInformation(line)

        for i in range(0, len(information), 2):
            if i == 0:
                dict["Game"] = int(information[1])
                continue

            if dict[str(information[i+1])] < int(information[i]):
                dict[str(information[i+1])] = int(information[i])
        
        result += dict["red"] * dict["green"] * dict["blue"]

# Part one
# with open(file_path, 'r') as file:
#     for line in file:
#         dict = {"Game": 0, "red": 0, "blue":0, "green": 0}
#         information = retriveInformation(line)

#         for i in range(0, len(information), 2):
#             if i == 0:
#                 dict["Game"] = int(information[1])
#                 continue

#             if dict[str(information[i+1])] < int(information[i]):
#                 dict[str(information[i+1])] = int(information[i])
        
#         if dict["red"] <= 12 and dict["green"] <= 13 and dict["blue"] <= 14:
#             result += dict["Game"]

print(result)