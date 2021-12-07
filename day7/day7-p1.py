import time


def parse_input_to_dict(s):
    d = {}
    s_list = list(map(lambda a: int(a), s[0].split(',')))

    for val in s_list:
        d.setdefault(val, 0)
        d[val] += 1

    return d


def init_min_fuel(d):  # Find required fuel to move crabs to position 0
    total_fuel = 0

    for key, val in d.items():
        total_fuel += key * val

    return total_fuel


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    crabs = parse_input_to_dict(inputs)
    min_fuel = init_min_fuel(crabs)

    for pos in range(max(crabs.keys()) + 1):
        total_fuel = 0

        for key, val in crabs.items():
            total_fuel += abs(key - pos) * val

        min_fuel = total_fuel if total_fuel < min_fuel else min_fuel

    print(min_fuel)


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
