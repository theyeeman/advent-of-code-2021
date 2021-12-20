import time


def main():
    # inputs = standard_func.get_input_as_str('input.txt')
    inputs = standard_func.get_input_as_str('test.txt')
    
    # Code goes here


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
Brainstorming

- get input as grid
    - 2d array of ints
- value greater than 9 means flash and increase surrounding cells by 1
- an octopus can only flash at most once per step
    - flashing means energy back to 0
- each step all energy increased by 1
    - so maybe increment all cells and then check for cells > 9, and if yes, set to 0 and increment all surrounding cells
    - need a way to mark cells that flash so they dont increment again
- since part 1 asks for 100 steps, part 2 probably asks for an even larger number of steps
- can't just loop through all cells consecutively since current cell could impact a previous cell
'''