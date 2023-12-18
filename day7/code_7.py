test_path = "test.txt"
file_path = "input.txt"

hands = []

with open(file_path, 'r') as file: 
    for line in file:
        word_list = line.split()
        hands.append((word_list[0], int(word_list[1])))

five_kind = []
four_kind = []
fullhouse = []
three_kind = []
two_pair = []
one_pair = []
high_card = []

power_dict = { "J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "Q": 11, "K": 12, "A": 13}

def find_optimal_hand(hand, hand_string):
    values = list(hand.values())
    keys = list(hand.keys())

    index_to_remove = keys.index("J")
    del values[index_to_remove]
    del keys[index_to_remove]

    modified_hand = hand_string

    if 4 in values: 
        modified_hand = hand_string.replace("J", keys[values.index(4)])
        return modified_hand
    
    if 3 in values: 
        modified_hand = hand_string.replace("J", keys[values.index(3)])
        return modified_hand
    
    if values.count(2) > 1:
        if power_dict[keys[0]] > power_dict[keys[1]]:
            modified_hand = hand_string.replace("J", keys[0])
        else:
            modified_hand = hand_string.replace("J", keys[1])
        return modified_hand
    
    if values.count(2) == 1:
        modified_hand = hand_string.replace("J", keys[values.index(2)])
        return modified_hand
    
    max_key = "J"
    for key in keys:
        if power_dict[key] > power_dict[max_key]:
            max_key = key

    modified_hand = hand_string.replace("J", max_key)
    return modified_hand

hand = {}


for i in range(len(hands)):
    current_cards = hands[i][0]

    # Only for part 2
    # if "J" in current_cards:
    #     for j in current_cards:
    #         if j in hand:
    #             hand[j] += 1
    #         else :
    #             hand[j] = 1

        
    #     current_cards = find_optimal_hand(hand, current_cards)
    #     hand = {}

    for j in current_cards:
        if j in hand:
            hand[j] += 1
        else :
            hand[j] = 1
    

    values = list(hand.values())

    if 5 in values: five_kind.append(hands[i])
    elif 4 in values: four_kind.append(hands[i])
    elif 3 in values and 2 in values: fullhouse.append(hands[i])
    elif 3 in values: three_kind.append(hands[i])
    elif values.count(2) > 1: two_pair.append(hands[i])
    elif 2 in values: one_pair.append(hands[i])
    else: high_card.append(hands[i])

    hand = {}


alphabet = "AKQT98765432J"
custom_order = {char: index for index, char in enumerate(alphabet)}

def custom_sort(tuple_item):
    return [custom_order[char] for char in tuple_item[0]]


all_hands_by_kind = [five_kind, four_kind, fullhouse, three_kind, two_pair, one_pair, high_card]

all_sorted = []

for kind in all_hands_by_kind:
    if not kind:
        continue

    all_sorted.extend(sorted(kind, key=custom_sort))

result = 0

all_sorted.reverse()
for i in range(len(all_sorted)):
    result += all_sorted[i][1] * (i + 1)

print(result)