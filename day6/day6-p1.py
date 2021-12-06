import time


def parse_input(inputs):
    return list(map(lambda a : int(a), inputs[0].split(',')))


def get_fish_dict(fish_input):
    fish_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
    }

    for day in fish_input:
        fish_dict[day] += 1

    return fish_dict


def process_dict(d):
    day_0 = d[0]

    for i in range(0, 8):
        d[i] = d[i + 1]

    d[8] = day_0
    d[6] += day_0

    # d_new = {
    #     0: 0,
    #     1: 0,
    #     2: 0,
    #     3: 0,
    #     4: 0,
    #     5: 0,
    #     6: 0,
    #     7: 0,
    #     8: 0,
    # }

    # for i in range(7, -1, -1):
    #     d_new[i] = d_old[i + 1]

    # d_new[8] = d_old[0]
    # d_new[6] += d_old[0]

    # return d_new


    # for i in range(8, 0, -1):
    #     amount = d[i]
    #     d[i] -= amount
    #     d[i - 1] += amount

    # amount = d[0]
    # d[0] -= amount
    # d[8] += amount
    # d[6] += amount


def sum_fish(d):
    return sum(d.values())


def main():
    # inputs = standard_func.get_input_as_str('input.txt')
    inputs = standard_func.get_input_as_str('test.txt')
    fish_input = parse_input(inputs)
    fish_dict = get_fish_dict(fish_input)
    days = 18
    # print(fish_input)
    # print(fish_dict)

    for _ in range(days):
        process_dict(fish_dict)

    print(sum_fish(fish_dict))


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

'''
brainstorming

create a dict where {key: val} = {fish timer: num fish}
each day, just move all the fish from day n to day n-1, and for fish at day 0, set that amount to 0 and add that amount to day 8
    need to start with highest fish timer value and work down to day 0
'''