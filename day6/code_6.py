import math

timelist = [53, 89, 76, 98]
distancelist = [313, 1090, 1214, 1201]

possibilitieslist = []

for race in range(0, len(timelist), 1):
    possibilities = 0
    time = timelist[race]
    distance = distancelist[race]
    halfway = math.ceil(time / 2)

    for i in range(halfway):
        if (time - i) * i > distance:
            possibilities += 2

    if time % 2 == 0:
        if time * time > distance:
            possibilities += 1

    possibilitieslist.append(possibilities)

print(possibilitieslist)

result = 1

# Multiply each integer in the list
for num in possibilitieslist:
    result *= num

print(result)

# Part two
# timelist = [53897698]#[7, 15, 30]
# distancelist = [313109012141201]#[9, 40, 200]

# possibilitieslist = []

# for race in range(0, len(timelist), 1):
#     possibilities = 0
#     time = timelist[race]
#     distance = distancelist[race]
#     halfway = math.ceil(time / 2)

#     for i in range(halfway):
#         if (time - i) * i > distance:
#             possibilities += 2

#     if time % 2 == 0:
#         if time * time > distance:
#             possibilities += 1

#     possibilitieslist.append(possibilities)

# result = 1

# # Multiply each integer in the list
# for num in possibilitieslist:
#     result *= num

# print(result)