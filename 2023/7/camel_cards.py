'''
step 0: parse input into hands and bids
step 1: order hands !make sure their bids stay with them!
step 2: get sumation of hand rank * bid
'''
card_types = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', 
'6', '5', '4', '3', '2']
card_types_to_value = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, 
'9': 9, '8': 8, '7': 7, 
'6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
hand_type_to_value = {
    'five-of-a-kind': 6,
    'four-of-a-kind': 5,
    'full-house': 4,
    'three-of-a-kind': 3,
    'two-pair': 2,
    'one-pair': 1,
    'high-card': 0
}
class Hand:
    def __init__(self, hand, bid):
        self.hand = hand
        self.hand_type = self.determine_hand_type(hand)
        self.bid = int(bid)
    def determine_hand_type(self, hand):
        # Find x-of-a-kinds.
        quantities = []
        cards_remaining = 5
        for card_type in card_types:
            quantity = hand.count(card_type)
            if quantity:
                quantities.append(quantity)
                cards_remaining -= quantity
        # Determine hand types based off of x-of-a-kinds.
        if 5 in quantities:
            return 'five-of-a-kind'
        elif 4 in quantities:
            return 'four-of-a-kind'
        elif 3 in quantities and 2 in quantities:
            return 'full-house'
        elif 3 in quantities:
            return 'three-of-a-kind'
        elif 2 in quantities and quantities.count(2) == 2:
            return 'two-pair'
        elif 2 in quantities:
            return 'one-pair'
        return 'high-card'

def compare_hands(hand_1, hand_2):
    # Comparing hand types.
    if hand_type_to_value[hand_1.hand_type] > hand_type_to_value[hand_2.hand_type]:
        return 1
    elif  hand_type_to_value[hand_1.hand_type] < hand_type_to_value[hand_2.hand_type]:
        return -1
    # Compare cards.
    for idx in range(len(hand_1.hand)):
        if card_types_to_value[hand_1.hand[idx]] > card_types_to_value[hand_2.hand[idx]]:
            return 1
        elif card_types_to_value[hand_1.hand[idx]] < card_types_to_value[hand_2.hand[idx]]:
            return -1
    # Equal hands.
    return 0

def merge_sort(array):
    if len(array) > 1:
        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        # Sort the two halves
        merge_sort(L)
        merge_sort(M)
        i = j = k = 0
        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if compare_hands(L[i], M[j]) == 1:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1
        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

test_input = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

if __name__ == '__main__':
    cards = test_input.split('\n')
    with open('2023/7/input_camel_cards.txt') as f:
        cards = f.read().split('\n')
    hands = []
    # Parse hands and bids.
    for line in cards:
        if len(line) < 1:
            continue
        hand, bid = line.split(' ')
        hands.append(Hand(hand, bid))
    # Sort hands.
    merge_sort(hands)
    # Calculate sum of hand rank * bid
    total = 0
    rank = len(hands)
    for hand in hands:
        total += rank * hand.bid
        rank -= 1
    print(total)
