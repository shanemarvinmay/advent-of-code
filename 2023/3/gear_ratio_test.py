import gear_ratios

diagonals = '''........*.
100..200..
...*......'''.split('\n')

verticals = '.*1$.'.split('\n')

only_number = '''...
.1.
...'''.split('\n')

lines = gear_ratios.test_input.split('\n')

def test_get_symbol_and_number_data():
    expected_symbols = {1: {3}, 3: {6}, 4: {3}, 5: {5}, 8: {3, 5}}
    expected_numbers = {0: [{'number': 467, 'start_col': 0, 'end_col': 2}, {'number': 114, 'start_col': 5, 'end_col': 7}], 2: [{'number': 35, 'start_col': 2, 'end_col': 3}, {'number': 633, 'start_col': 6, 'end_col': 8}], 4: [{'number': 617, 'start_col': 0, 'end_col': 2}], 5: [{'number': 58, 'start_col': 7, 'end_col': 8}], 6: [{'number': 592, 'start_col': 2, 'end_col': 4}], 7: [{'number': 755, 'start_col': 6, 'end_col': 8}], 9: [{'number': 664, 'start_col': 1, 'end_col': 3}, {'number': 598, 'start_col': 5, 'end_col': 7}]}

    symbols, numbers = gear_ratios.get_symbol_and_number_data(lines)

    assert symbols == expected_symbols, 'Checking symbols'
    assert numbers == expected_numbers, 'Checking numbers'

def test_get_total_numbers_with_boarding_symbols_diagonals():
    expected_total = 300
    symbols, numbers = gear_ratios.get_symbol_and_number_data(diagonals)

    total = gear_ratios.get_total_numbers_with_boarding_symbols(symbols, numbers)

    assert total == expected_total, 'Checking total diagonals'

def test_get_total_numbers_with_boarding_symbols_verticals():
    expected_total = 1
    symbols, numbers = gear_ratios.get_symbol_and_number_data(verticals)

    total = gear_ratios.get_total_numbers_with_boarding_symbols(symbols, numbers)

    assert total == expected_total, 'Checking total verticals'

def test_get_total_numbers_with_boarding_symbols_only_number():
    expected_total = 0
    symbols, numbers = gear_ratios.get_symbol_and_number_data(only_number)

    total = gear_ratios.get_total_numbers_with_boarding_symbols(symbols, numbers)

    assert total == expected_total, 'Checking total only numbers'

def test_get_total_numbers_with_boarding_symbols_test_input():
    expected_total = 4361
    symbols, numbers = gear_ratios.get_symbol_and_number_data(lines)

    total = gear_ratios.get_total_numbers_with_boarding_symbols(symbols, numbers)

    assert total == expected_total, 'Checking total with test input'