import time


def get_oxygen_rating(inputs):
    for i in range(len(inputs[0])):
        if len(inputs) == 1:
            break

        remove_digit = get_least_common_bin_digit(inputs, i)
        remove_row(inputs, i, remove_digit)

    return inputs[0]


def get_scrubber_rating(inputs):
    for i in range(len(inputs[0])):
        if len(inputs) == 1:
            break

        remove_digit = get_most_common_bin_digit(inputs, i)
        remove_row(inputs, i, remove_digit)

    return inputs[0]


def get_most_common_bin_digit(inputs, char_pos):
    num_0 = 0
    num_1 = 0

    for input in inputs:
        if input[char_pos] == '0':
            num_0 += 1
        else:
            num_1 += 1

    if num_0 > num_1:
        return '0'
    else:
        return '1'


def get_least_common_bin_digit(inputs, char_pos):
    num_0 = 0
    num_1 = 0

    for input in inputs:
        if input[char_pos] == '0':
            num_0 += 1
        else:
            num_1 += 1
    
    if num_0 <= num_1:
        return '0'
    else:
        return '1'


def remove_row(inputs, char_pos, bin_val):
    i = 0

    while i < len(inputs):
        if inputs[i][char_pos] == bin_val:
            inputs.pop(i)
        else:
            i += 1


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    #inputs = standard_func.get_input_as_str('test.txt')
    backup = inputs.copy()

    oxygen_rating = int(get_oxygen_rating(backup), 2)
    scrubber_rating = int(get_scrubber_rating(inputs), 2)

    print(oxygen_rating * scrubber_rating)


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
