import time


def plot_vertical(coords, x1, y1, x2, y2):
    x = x1
    y_min = min(y1, y2)
    y_max = max(y1, y2)

    for y in range(y_min, y_max + 1):
        coords.setdefault((x, y), 0)
        coords[(x, y)] += 1


def plot_horizontal(coords, x1, y1, x2, y2):
    y = y1
    x_min = min(x1, x2)
    x_max = max(x1, x2)

    for x in range(x_min, x_max + 1):
        coords.setdefault((x, y), 0)
        coords[(x, y)] += 1


def is_vertical(x1, y1, x2, y2):
    return x1 == x2


def is_horizontal(x1, y1, x2, y2):
    return y1 == y2


def parse_input_row(row):
    s = row.split(' ')
    x1, y1 = s[0].split(',')
    x2, y2 = s[2].split(',')

    return (int(x1), int(y1), int(x2), int(y2))


def print_dict(d):
    for k in d.keys():
        print(f'{k} : {d[k]}')


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    coords = {}
    count = 0
    
    for input in inputs:
        # x1, y1, x2, y2 = parse_input_row(input)

        # if is_horizontal(x1, y1, x2, y2):
        #     print(f'{x1} {y1} {x2} {y2} horizontal')
        # elif is_vertical(x1, y1, x2, y2):
        #     print(f'{x1} {y1} {x2} {y2} vertical')
        x1, y1, x2, y2 = parse_input_row(input)

        if is_horizontal(x1, y1, x2, y2):
            plot_horizontal(coords, x1, y1, x2, y2)
        elif is_vertical(x1, y1, x2, y2):
            plot_vertical(coords, x1, y1, x2, y2)
        else:
            continue
    
    # print_dict(coords)

    for v in coords.values():
        if v >= 2:
            count += 1

    print(count)
    

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
brain storming

parse input into format (x1, y1, x2, y2)
helper function to check if line horizontal
helper function to check if line vertical
helper function to add horizontal line to dict
helper function to add vertical line to dict
dictionary with {key, val} = {(coord), count}
'''