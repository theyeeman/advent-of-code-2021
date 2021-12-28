import time


def parse_input(inputs, letter_count):
    poly_string = inputs[0]

    for char in poly_string:
        letter_count.setdefault(char, 0)
        letter_count[char] += 1

    curr_pairs = parse_poly_string_to_pairs(poly_string)
    pair_insert_rule = {}

    for input in inputs:
        test = input.split(' -> ')

        if len(test) == 2:
            pair_insert_rule.update({test[0]: test[1]})

    return curr_pairs, pair_insert_rule


def parse_poly_string_to_pairs(poly_string):
    pairs = {}

    for i in range(len(poly_string) - 1):
        curr_pair = poly_string[i] + poly_string[i+1]
        pairs.setdefault(curr_pair, 0)
        pairs[curr_pair] += 1

    return pairs


def get_new_pairs(curr_pair, pair_insert, letter_count, pair_count):
    insert_letter = pair_insert[curr_pair]
    letter_count.setdefault(insert_letter, 0)
    letter_count[insert_letter] += pair_count

    return [curr_pair[0] + insert_letter, insert_letter + curr_pair[1]]


def get_least_and_most_common_letter_count(letter_count):
    least_counted_letter = min(letter_count, key=lambda key: letter_count[key])
    most_counted_letter = max(letter_count, key=lambda key: letter_count[key])

    return letter_count[least_counted_letter], letter_count[most_counted_letter]


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    letter_count = {}  # letter_count is injected into functions parse_input and get_new_pairs to keep track of number of letters
    curr_pairs_dict, pair_insert_rules = parse_input(inputs, letter_count)
    steps = 10
    temp_dict = {}

    for _ in range(steps):
        for curr_pair, curr_pair_count in curr_pairs_dict.items():
            new_pairs = get_new_pairs(curr_pair, pair_insert_rules, letter_count, curr_pair_count)
            
            for pair in new_pairs:
                temp_dict.setdefault(pair, 0)
                temp_dict[pair] += curr_pair_count

        curr_pairs_dict = temp_dict.copy()
        temp_dict.clear()

    least_count, most_count = get_least_and_most_common_letter_count(letter_count)
    print(most_count - least_count)


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
