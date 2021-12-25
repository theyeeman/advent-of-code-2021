import time


def is_cave_small_letter(cave):
    return cave.islower()


def get_caves_to_visit(cave_list, seen):
    return list(set(cave_list).difference(seen))


def dfs(curr_cave, all_caves, seen):
    caves_to_visit = get_caves_to_visit(all_caves[curr_cave], seen)
    num_paths = 0

    if curr_cave == 'end':
        return 1
    elif len(caves_to_visit) == 0:
        return 0
    else:
        if is_cave_small_letter(curr_cave):
            seen.add(curr_cave)

        for cave in caves_to_visit:
            num_paths += dfs(cave, all_caves, seen.copy())
        
        return num_paths


def parse_input(inputs):
    cave_dict = {}

    for input in inputs:
        cave, connected = input.split('-')
        cave_dict.setdefault(cave, [])
        cave_dict.setdefault(connected, [])
        cave_dict[cave].append(connected)
        cave_dict[connected].append(cave)

    return cave_dict


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    
    cave_dict = parse_input(inputs)
    seen = set(['start'])

    print(dfs('start', cave_dict, seen))


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
