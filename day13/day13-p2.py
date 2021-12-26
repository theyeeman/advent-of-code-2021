import time


def _parse_input_to_fold_list(inputs):
    folds = []

    for input in inputs:
        parsed = input.split('=')

        if len(parsed) == 2:
            folds.append((parsed[0][-1], int(parsed[1])))

    return folds
        

def _parse_input_to_pos_set(inputs):
    pos = set()

    for input in inputs:
        if input == '':
            break

        x, y = input.split(',')
        pos.add((int(x), int(y)))

    return pos


def parse_input(inputs):
    pos = _parse_input_to_pos_set(inputs)
    folds = _parse_input_to_fold_list(inputs)
    
    return pos, folds


def fold_left(pos, x_line):
    pos_list = list(pos)

    for p in pos_list:
        x, y = p

        if x > x_line:
            folded_x = x_line - abs(x_line - x)
            pos.remove(p)
            pos.add((folded_x, y))


def fold_up(pos, y_line):
    pos_list = list(pos)

    for p in pos_list:
        x, y = p

        if y > y_line:
            folded_y = y_line - abs(y_line - y)
            pos.remove(p)
            pos.add((x, folded_y))


def draw_grid(pos):
    max_x = max(pos, key=lambda p : p[0])[0] + 1
    max_y = max(pos, key=lambda p : p[1])[1] + 1
    
    for j in range(max_y):
        row = ''
        for i in range(max_x):
            if (i, j) in pos:
                row += '#'
            else:
                row += '.'

        print(row)


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    
    pos, folds = parse_input(inputs)
    
    for fold_line, line_num in folds:
        if fold_line == 'y':
            fold_up(pos, line_num)
        else:
            fold_left(pos, line_num)

    draw_grid(pos)


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
