import re
import os

test_path = "test.txt"
file_path = "input.txt"
lasse_path = "lasse.txt"

node_map = {}
instructions = ""
starting_nodes = []
ending_nodes = []

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
            ending_nodes.append(information[0])

instructions = instructions.replace("\n", "")
instlist = list(instructions)

import math
from functools import reduce

def find_steps_to_Z(start_node, end_nodes, pattern):
    # Given the start and end nodes, find the number of steps required to reach the end node
    steps = 0
    current_node = start_node
    searching = True
    znode = ""

    while searching:
        for c in pattern:
            steps += 1

            if c == "L":
                current_node = node_map[current_node][0]
            elif c == "R":
                current_node = node_map[current_node][1]

            if znode == current_node:
                searching = False
                break

            if end_nodes.__contains__(current_node):
                znode = current_node
                steps = 0
            

    return steps

def find_steps_to_Z_with_pattern(starts, ends, pattern):
    steps_list = []
    for i in range(len(starts)):
        steps_list.append(find_steps_to_Z(starts[i], ends, pattern))

    lcm_result = reduce(math.lcm, steps_list)

    return lcm_result

# Find steps to Z with the specified pattern
result = find_steps_to_Z_with_pattern(starting_nodes, ending_nodes, instructions)

print(result)