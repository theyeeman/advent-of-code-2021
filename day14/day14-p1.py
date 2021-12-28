import time


def parse_input(inputs, letter_count):
    for char in inputs[0]:
        letter_count.setdefault(char, 0)
        letter_count[char] += 1

    curr_pairs = parse_poly_string_to_pairs(inputs[0])
    pair_insert = {}

    for input in inputs:
        test = input.split(' -> ')

        if len(test) == 2:
            pair_insert.update({test[0]: test[1]})

    return curr_pairs, pair_insert


def parse_poly_string_to_pairs(poly_string):
    pairs = {}

    for i in range(len(poly_string) - 1):
        curr_pair = poly_string[i] + poly_string[i+1]
        pairs.setdefault(curr_pair, 0)
        pairs[curr_pair] += 1

    return pairs


def get_new_pairs(curr_pair, pair_insert, letter_count, val):
    insert_letter = pair_insert[curr_pair]
    # print('adding', insert_letter, 'to insert_letter')
    letter_count.setdefault(insert_letter, 0)
    letter_count[insert_letter] += val

    return [curr_pair[0]+insert_letter, insert_letter+curr_pair[1]]


def get_least_and_most_common_letter_count(letter_count):
    least_counted_letter = min(letter_count, key=lambda key: letter_count[key])
    most_counted_letter = max(letter_count, key=lambda key: letter_count[key])
    print(least_counted_letter, most_counted_letter)

    return letter_count[least_counted_letter], letter_count[most_counted_letter]


def main():
    # inputs = standard_func.get_input_as_str('input.txt')
    inputs = standard_func.get_input_as_str('test.txt')
    steps = 10
    temp_dict = {}
    letter_count = {}
    curr_pairs, pair_insert = parse_input(inputs, letter_count)

    for _ in range(steps):
        # print('step', _)
        # print('letter_count', letter_count)
        # print('curr_pairs', curr_pairs)
        for curr_pair, val in curr_pairs.items():
            new_pairs = get_new_pairs(curr_pair, pair_insert, letter_count, val)
            
            for pair in new_pairs:
                temp_dict.setdefault(pair, 0)
                temp_dict[pair] += val

        
        curr_pairs = temp_dict.copy()
        temp_dict.clear()

    # print('letter_count', letter_count)
    # print('curr_pairs', curr_pairs)
    print(get_least_and_most_common_letter_count(letter_count))


# Boilerplate code below
class standard_func:
    def get_input_as_int(filename):
        with open(filename) as f:
            return list(map(lambda a : int(a), list((f.read()).split("\n"))))

    def get_input_as_str(filename):
        with open(filename) as f:
            return list((f.read()).split("\n"))

    def print_performance(start, end):
        print('Execution time (s):', round((end - start), 3))


if __name__ == "__main__":
    perf_counter_start = time.perf_counter()
    main()
    perf_counter_end = time.perf_counter()
    standard_func.print_performance(perf_counter_start, perf_counter_end)
