import time


def pretty_print(matrix):
    print('*************************')
    
    for row in matrix:
        print(row)

    print('*************************')


def parse_input_into_matrix(inputs):
    matrix = []

    for row in inputs:
        matrix.append([int(c) for c in row])

    return matrix


def duplicate_matrix(matrix):
    duplicate = [row.copy() for row in matrix]

    return duplicate


def precompute_path_sums(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == 0 and col == 0:  # start case -> skip computation
                continue
            elif row == 0 and col > 0:
                matrix[row][col] += matrix[row][col-1]
            elif row > 0 and col == 0:
                matrix[row][col] += matrix[row-1][col]
            else:
                matrix[row][col] += min(matrix[row-1][col], matrix[row][col-1])


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    
    matrix = parse_input_into_matrix(inputs)
    matrix[0][0] = 0  # set to 0 since we don't count the starting position
    dp = duplicate_matrix(matrix)
    precompute_path_sums(dp)
    print(dp[-1][-1])

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
