test_input_1 = '''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)'''

test_input_2 = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''

'''
steps 0: parse input steps
step 1: parse input map
step 2: execute and count steps'''

def parse_input(input):
    lines = input.split('\n')
    turns = lines[0]
    
    nodes = dict()
    for i in range(2, len(lines)):
        if len(lines[i]) < 1:
            continue
        # key 
        key, values = lines[i].split(' = ')
        # values
        left, right = values.split(', ')
        nodes[key] = {'L': left[1:], 'R': right[:-1]}
    
    return turns, nodes

def count_steps(turns, nodes):
    node = 'AAA'
    steps, turn_idx = 0, 0
    while node != 'ZZZ':
        if turn_idx >= len(turns):
            turn_idx = 0
        # print(node, '->', turns[turn_idx], '->', nodes[node][turns[turn_idx]])
        node = nodes[node][turns[turn_idx]]
        turn_idx += 1
        steps += 1
    return steps

if __name__ == '__main__': 
    with open('2023/8/input_map.txt') as f:
            input = f.read()

    turns, nodes = parse_input(input)


    print(count_steps(turns, nodes))