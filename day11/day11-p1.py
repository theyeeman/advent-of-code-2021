import time


def parse_input(inputs):
    grid = []
    for row in inputs:
        grid.append([int(x) for x in row])

    return grid


def increment_all_cells(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] += 1


def get_flashed_cell_surrounding_flashes(grid, x, y):
    flash = []

    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                continue

            grid[i][j] += 1

            if grid[i][j] > 9:
                flash.append((i, j))
                grid[i][j] = 0

    return flash


def print_grid(grid):
    print('*****************************')
    for row in grid:
        print(row)


def get_cells_that_will_flash(grid):
    flash = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 9:
                flash.append((i, j))
                grid[i][j] = 0

    return flash


def do_surrounding_flash_cell(grid, flash):
    num_flash = 0

    while flash:
        x, y = flash.pop()
        new_flash = get_flashed_cell_surrounding_flashes(grid, x, y)
        flash += new_flash
        num_flash += len(new_flash)

    return num_flash


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    grid = parse_input(inputs)
    num_flash = 0
    steps = 100

    for _ in range(steps):
        increment_all_cells(grid)
        flash = get_cells_that_will_flash(grid)
        num_flash += len(flash)
        num_flash += do_surrounding_flash_cell(grid, flash)

    print(num_flash)


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
