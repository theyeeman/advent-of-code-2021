import time


def is_cave_small_letter(cave):
    return cave.islower()


def get_caves_to_visit(cave_list, seen):
    #return list(set(cave_list).difference(seen))
    new_list = []

    for cave in cave_list:
        if cave not in seen:
            new_list.append(cave)

    return sorted(new_list)


def dfs(curr_cave, all_caves, seen, iterloop, path):
    caves_to_visit = get_caves_to_visit(all_caves[curr_cave], seen)  # if curr_cave != 'end' else []
    num_paths = 0

    #print(f'curr_cave {curr_cave}, caves_to_visit {caves_to_visit}, iterloop {iterloop}, path {path}')
    #print(path)
    if is_cave_small_letter(curr_cave):
        seen.add(curr_cave)

    if curr_cave == 'end':
        #print('end reached')
        #print(path)
        return 1
    elif len(caves_to_visit) == 0:
        #print('stuck')
        return 0
    else:
        for cave in caves_to_visit:
            num_paths += dfs(cave, all_caves, seen.copy(), iterloop + 1, path + ' ' + cave)
        
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
    # inputs = standard_func.get_input_as_str('input.txt')
    inputs = standard_func.get_input_as_str('test.txt')
    
    cave_dict = parse_input(inputs)
    seen = set(['start'])

    print(cave_dict)
    print(dfs('start', cave_dict, seen, 0, 'start'))


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
import time


def parse_input(inputs):
    cave_dict = {}

    for input in inputs:
        cave, connected = input.split('-')
        cave_dict.setdefault(cave, [])
        cave_dict.setdefault(connected, [])
        cave_dict[cave].append(connected)
        cave_dict[connected].append(cave)

    return cave_dict


def get_caves_to_visit(cave_list, seen):
    #return list(set(cave_list).difference(seen))
    new_list = []

    for cave in cave_list:
        if cave not in seen:
            new_list.append(cave)

    return new_list


def main():
    # inputs = standard_func.get_input_as_str('input.txt')
    inputs = standard_func.get_input_as_str('test.txt')
    
    cave_dict = parse_input(inputs)
    seen = set(['start'])
    caves_to_visit = cave_dict['start']
    num_paths = 0
    print(cave_dict)
    

    while caves_to_visit:
        print(caves_to_visit)
        curr_cave = caves_to_visit.pop()
        # print(caves_to_visit)
        # print(type(caves_to_visit))
        print(curr_cave)
        # print(type(curr_cave))

        if curr_cave == 'start':
            continue

        if curr_cave == 'end':
            num_paths += 1
            continue
        
        # if curr_cave in seen:
        #     continue

        if curr_cave.islower() and curr_cave != 'end':
            seen.add(curr_cave)
        
        caves_to_visit += get_caves_to_visit(cave_dict[curr_cave], seen)

    print(num_paths)

        

        


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
