import scratchcards

def test_parse_numbers():
    numbers_str = '87 83 26 28 32'
    expected_numbers = [87, 83, 26, 28, 32]
    assert scratchcards.parse_numbers(numbers_str) == expected_numbers, 'Parse string of numbers into a list of ints.'

def test_get_card_score_no_score():
    card = 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36'
    assert scratchcards.get_card_score(card) == 0, 'Score card worth no points'

def test_get_card_score_with_score():
    card = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'
    assert scratchcards.get_card_score(card) == 8, 'Score card worth points'

def test_get_cards_total_score():
    cards = scratchcards.test_input.split('\n')
    assert scratchcards.get_cards_total_score(cards) == 13, 'Evaluating cards with various scores'

