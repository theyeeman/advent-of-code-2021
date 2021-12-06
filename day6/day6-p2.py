import time


def parse_input(inputs):
    return list(map(lambda a : int(a), inputs[0].split(',')))


def get_fish_list(fish_input):
    fish_list = [0] * 9

    for day in fish_input:
        fish_list[day] += 1

    return fish_list


def process_list(fish):
    day_0 = fish[0]
    fish.pop(0)
    fish.append(day_0)
    fish[6] += day_0


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    fish_input = parse_input(inputs)
    fish_list = get_fish_list(fish_input)
    days = 256

    for _ in range(days):
        process_list(fish_list)

    print(sum(fish_list))


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