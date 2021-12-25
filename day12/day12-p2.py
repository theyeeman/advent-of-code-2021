import time


def is_cave_small_letter(cave):
    return cave.islower()


def get_caves_to_visit(cave_list, seen):
    to_visit = []

    for cave in cave_list:
        if seen.get(cave, 0) >= 2:
            continue

        to_visit.append(cave)

    return to_visit


def is_too_many_small_caves(seen):
    count = 0

    for key, val in seen.items():
        if key == 'start':
            continue
        if val >= 2:
            count += 1

    return count > 1

def dfs(curr_cave, all_caves, seen):
    caves_to_visit = get_caves_to_visit(all_caves[curr_cave], seen)
    num_paths = 0  

    if curr_cave == 'end':
        return 1
    elif len(caves_to_visit) == 0:
        return 0
    else:
        if is_cave_small_letter(curr_cave):
            seen.setdefault(curr_cave, 0)
            seen[curr_cave] += 1

        if is_too_many_small_caves(seen):  # can only visit one small cave twice
            return 0

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
    seen = {'start': 1}

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
