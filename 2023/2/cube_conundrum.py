class ParsedGame:
    def __init__(self, line):
        self.game_id = self._parse_game_id(line)
        self.color_highest_count = self._parse_draws(line)
    def _parse_game_id(self, line):
        '''The game id will be found between the first space and the first ':'.'''
        first_space_idx = line.index(' ')
        first_colon_idx = line.index(':')
        game_id = line[first_space_idx + 1: first_colon_idx]
        return int(game_id)
    def _parse_draws(self, line):
        '''_parse_draws parses each draw that took place during the game. It returns the highest red, blue, and green ever drawn.'''
        color_highest_count = {'red': 0, 'green': 0, 'blue': 0}
        # Cutting off the game id segment of the line.
        line = line[line.index(':') + 1 :]
        # Iterating through the draws.
        for draw in line.split(';'):
            for count_color in draw.split(','):
                parts = count_color.strip().split(' ')
                try:
                    count = int(parts[0])
                    color = parts[1]
                except:
                    color, count = '', 0
                if color in color_highest_count and count > color_highest_count[color]:
                    color_highest_count[color] = count
        return color_highest_count
    def is_possible(self):
        if self.color_highest_count['red'] > 12:
            return False
        if self.color_highest_count['green'] > 13:
            return False
        if self.color_highest_count['blue'] > 14:
            return False
        return True

if __name__ == '__main__':
    test_input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
    file_data = ''
    with open('input_cube_conundrum.txt') as f:
        file_data = f.read()
    total = 0
    parsed_games = []
    for line in file_data.split('\n'):
        if len(line) < 1:
            continue
        parsed_game = ParsedGame(line)
        if parsed_game.is_possible():
            total += parsed_game.game_id
    # get answer
    print(total)