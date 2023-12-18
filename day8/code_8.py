import re
import os

test_path = "test.txt"
file_path = "input.txt"
lasse_path = "lasse.txt"

node_map = {}
instructions = ""
current_node = "AAA"
starting_nodes = []
ending_nodes = {}

pattern = re.compile(r'[a-zA-Z0-9]+')

def retriveInformation(input_string):
    return pattern.findall(input_string)

with open(file_path, 'r') as file: 
    for line in file:
        
        if line == "\n":
            continue

        if instructions == "":
            instructions = line
            continue

        information = retriveInformation(line)

        node_map[information[0]] = (information[1], information[2])
        
        nodechars = list(information[0]) 
        if nodechars[2] == "A":
            starting_nodes.append(information[0])
        elif nodechars[2] == "Z":
            ending_nodes[information[0]] = 0


still_searching = True
steps = 0
backup = instructions
instructions = instructions.replace("\n", "")
instructions = instructions.replace("L", "0")
instructions = instructions.replace("R", "1")
char_list = list(instructions)
int_list = [int(char) for char in char_list]

def check_if_ending_node(node):
    if node in ending_nodes:
        return True
    else:
        return False

print_break = 500 * len(int_list)

while still_searching:
    if steps % print_break == 0:
        print(steps)

    for i in int_list:
        
        for j in range(len(starting_nodes)):
            starting_nodes[j] = node_map[starting_nodes[j]][i]

        steps += 1

        am_i_done = all(check_if_ending_node(node) for node in starting_nodes)

        if am_i_done:
            still_searching = False
            break


    

