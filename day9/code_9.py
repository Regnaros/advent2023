import os

file_path = "input.txt"
test_path = "test.txt"

script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

histories = []
with open(file_path, 'r') as file: 
    for line in file:
        history =  line.replace("\n", "").split(sep=" ")

        history_int = list(map(int, history))
        histories.append(history_int)

extrapolation = []
next_increment = []
for history in histories:
    not_all_zeros = True
    extrapolation = [history]

    while not_all_zeros:
        extrapolation_step = []
        current_step = extrapolation[-1]

        for i in range(len(current_step) - 1, 0, -1):
            extrapolation_step.insert(0, current_step[i] - current_step[i-1])
        
        extrapolation.append(extrapolation_step)
        if all(v == 0 for v in extrapolation_step):
            not_all_zeros = False
        
    for i in range (len(extrapolation)-1, 0, -1):
        extrapolation[i-1].insert(0, extrapolation[i-1][0] - extrapolation[i][0])
    
    next_increment.append(extrapolation[0][0])


#Part one
# for history in histories:
#     not_all_zeros = True
#     extrapolation = [history]

#     while not_all_zeros:
#         extrapolation_step = []
#         current_step = extrapolation[-1]

#         for i in range(1, len(current_step), 1):
#             extrapolation_step.append(current_step[i] - current_step[i-1])
        
#         extrapolation.append(extrapolation_step)
#         if all(v == 0 for v in extrapolation_step):
#             not_all_zeros = False
        
#     for i in range (len(extrapolation)-1, 0, -1):
#         extrapolation[i-1].append(extrapolation[i-1][-1] + extrapolation[i][-1])
    
#     next_increment.append(extrapolation[0][-1])

print(sum(next_increment))

