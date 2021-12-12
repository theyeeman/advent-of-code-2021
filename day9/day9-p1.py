import time


def is_lowest_adj_num(grid, x, y):
    x_min = x - 1 if x > 0 else 0
    x_max = x + 1 if x < len(grid) - 1 else x
    y_min = y - 1 if y > 0 else 0
    y_max = y + 1 if y < len(grid[0]) - 1 else y

    # print(f'call   grid[x][y]:{grid[x][y]}  x:{x}   y:{y}   x_min:{x_min}   x_max+1:{x_max + 1}   y_min:{y_min}   y_max+1:{y_max + 1}')
    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            # print(i, j, grid[i][j])

            if i == x and j == y:
                continue

            if grid[i][j] <= grid[x][y]:
                # print('not lowest')
                return False

    # print('is lowest')
    return True


def parse_input_to_grid(inputs):
    grid = []

    for input in inputs:
        grid.append(list(map(lambda a: int(a), input)))

    return grid


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    grid = parse_input_to_grid(inputs)
    risk_level = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_lowest_adj_num(grid, i, j):
                risk_level += grid[i][j] + 1

    print(risk_level)


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
