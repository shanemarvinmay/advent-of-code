'''--- Day 3: Gear Ratios ---

You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
'''

'''scratch
total = 0
symbol storage = {line num: set{col num}}
number storage = {line num: [{num: #, start col :#, end col: #}]}

lines = file content split \n

for line num in  range lines length
    line = lines[line num]
    cur_num= []
    for col num in range line length:
        char = line[col num]
        if char is digit 
            cur_num append char
        elsif cur num not empty
            num_str = cur num join ''
            num = int num str
            cur num = []
            # check if line num is in number storage
            num storage [line num] append {num: num, start: col - len(num str), end: col - 1}
        if char is not digit and char != '.'
            # check if line num is in symbol storage
            symbol storage [line num] add col num

for line num in number storage
    # check horizontal borders for symbols
    # check diagonal and veritcal borders for symbols
    # add numbers that touch symbols
'''
test_input = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
symbols = dict() # {line num: set{col num}}
numbers = dict() # {line num: [{num: #, start col :#, end col: #}]}
lines = test_input.split('\n')

# Getting symbols and numbers
for row in range(len(lines)):
    line = lines[row]
    cur_num = []
    for col in range(len(line)):
        char = line[col]
        if char.isdigit():
            cur_num.append(char)
        elif len(cur_num):
            num_str = ''.join(cur_num)
            cur_num = []
            if row not in numbers:
                numbers[row] = []
            numbers[row].append({'number': int(num_str), 'start_col': col - len(num_str), 'end_col': col})
        if char.isdigit() == False and char != '.':
            if row not in symbols:
                symbols[row] = set()
            symbols[row].add(col)

print('nums')
for row in numbers:
    print(row, numbers[row])

print('symbols')
for row in symbols:
    print(row, symbols[row])