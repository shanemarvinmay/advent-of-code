test_input = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4'''

# Attempt 2: range approach (better Big O space notation)
def extract_numbers_from_line(line):
    numbers = []
    for number in line.split(' '):
        numbers.append(int(number))
    return numbers

class Converter:
    def __init__(self, line) -> None:
        self.destination_start, self.source_start, self.range = extract_numbers_from_line(line)
    def is_in_range(self, value):
        diff = value - self.source_start
        if diff >= self.range or diff < 0:
            return False
        return True
    def convert(self, value):
        if self.is_in_range(value):
            diff = value - self.source_start
            return self.destination_start + diff
        else:
            return value

def generate_converters_for_setion(section):
    converters = []
    for line in section.split('\n'):      
        converters.append(Converter(line))
    return converters

def convert_values_with_section(values, section):
    section_converters = generate_converters_for_setion(section)
    for i in range(len(values)):
        value = values[i]
        for converter in section_converters:
            if converter.is_in_range(value):
                values[i] = converter.convert(value)
                break
    return values

if __name__ == '__main__':
    input = test_input
    with open('2023/5/input_seed.txt') as f:
        input = f.read()
    # breaking up the input
    start = input.index('seeds:') + len('seeds:')
    end = input.index('seed-to-soil map:')
    seed_section = input[start: end].strip()
    start = input.index('seed-to-soil map:') + len('seed-to-soil map:')
    end = input.index('soil-to-fertilizer map:')
    seed_to_soil_section = input[start: end].strip()
    start = input.index('soil-to-fertilizer map:') + len('soil-to-fertilizer map:')
    end = input.index('fertilizer-to-water map:')
    soil_to_fertilizer_section = input[start: end].strip()
    start = input.index('fertilizer-to-water map:') + len('fertilizer-to-water map:')
    end = input.index('water-to-light map:')
    fertilizer_to_water_section = input[start: end].strip()
    start = input.index('water-to-light map:') + len('water-to-light map:')
    end = input.index('light-to-temperature map:')
    water_to_light_section = input[start: end].strip()
    start = input.index('light-to-temperature map:') + len('light-to-temperature map:')
    end = input.index('temperature-to-humidity map:')
    light_to_temperature_section = input[start: end].strip()
    start = input.index('temperature-to-humidity map:') + len('temperature-to-humidity map:')
    end = input.index('humidity-to-location map:')
    temperature_to_humidity_section = input[start: end].strip()
    start = input.index('humidity-to-location map:') + len('humidity-to-location map:')
    humidity_to_location_section = input[start:].strip()
    seeds = extract_numbers_from_line(seed_section)
    print('seeds', seeds)
    soils = convert_values_with_section(seeds, seed_to_soil_section)
    print('soils', soils)
    fertilizers = convert_values_with_section(soils, soil_to_fertilizer_section)
    print('fertilizers', fertilizers)
    waters = convert_values_with_section(fertilizers, fertilizer_to_water_section)
    print('waters', waters)
    lights = convert_values_with_section(waters, water_to_light_section)
    print('lights', lights)
    temperatures = convert_values_with_section(lights, light_to_temperature_section)
    print('temperatures', temperatures)
    humidities = convert_values_with_section(temperatures, temperature_to_humidity_section)
    print('humidities', humidities)
    locations = convert_values_with_section(humidities, humidity_to_location_section)
    print('locations', locations)
    print('min location', min(locations))

    # Attempt 1: Hashmap approach (better Big O time notation)
    # def section_to_hashmap(section):
    #     hashmap = dict()
    #     for line in section.split('\n'):
    #         destination, source, span = extract_numbers_from_line(line)
    #         for i in range(span):
    #             hashmap[source + i] = destination + i
    #     return hashmap

    # def map_values(values, hashmap):
    #     new_values = []
    #     for value in values:
    #         if value not in hashmap:
    #             new_values.append(value)
    #         else:
    #             new_values.append(hashmap[value])
    #     return new_values

    # seed_to_soil = section_to_hashmap(seed_to_soil_section)
    # soil_to_fertilizer = section_to_hashmap(soil_to_fertilizer_section)
    # fertilizer_to_water = section_to_hashmap(fertilizer_to_water_section)
    # water_to_light = section_to_hashmap(water_to_light_section)
    # light_to_temperature = section_to_hashmap(light_to_temperature_section)
    # temperature_to_humidity = section_to_hashmap(temperature_to_humidity_section)
    # humidity_to_location = section_to_hashmap(humidity_to_location_section)

    # seeds = extract_numbers_from_line(seed_section)
    # print('seeds', seeds)
    # soil = map_values(seeds, seed_to_soil)
    # print('soil', soil)
    # fertilizer = map_values(soil, soil_to_fertilizer)
    # print('fertilizer', fertilizer)
    # water = map_values(fertilizer, fertilizer_to_water)
    # print('water', water)
    # light = map_values(water, water_to_light)
    # print('light', light)
    # temperature = map_values(light, light_to_temperature)
    # print('temperature', temperature)
    # humidity = map_values(temperature, temperature_to_humidity)
    # print('humidity', humidity)
    # location = map_values(humidity, humidity_to_location)
    # print('location', location)
    # print('min location', min(location))
