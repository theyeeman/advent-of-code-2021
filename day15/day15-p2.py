import time


def pretty_print(matrix):
    print('*************************')
    
    for row in matrix:
        print(row)

    print('*************************')


def pretty_print_stringified(matrix):
    print('*************************')
    
    for row in matrix:
        print(''.join([str(c) for c in row]))

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
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 and j == 0:  # start case -> skip computation
                continue
            elif i == 0 and j > 0:
                matrix[i][j] += matrix[i][j-1]
            elif i > 0 and j == 0:
                matrix[i][j] += matrix[i-1][j]
            else:
                matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])


def add_value_to_matrix(matrix, value):
    duplicate = duplicate_matrix(matrix)

    for i in range(len(duplicate)):
        for j in range(len(duplicate[0])):
            duplicate[i][j] += value

            if duplicate[i][j] > 9:
                duplicate[i][j] -= 9

    return duplicate


def add_value_to_row(row, value):
    duplicate = row.copy()

    for i in range(len(duplicate)):
        duplicate[i] += value

        if duplicate[i] > 9:
            duplicate[i] -= 9

    return duplicate


def expand_matrix(matrix, times):
    duplicate = duplicate_matrix(matrix)

    for t in range(1, times):  # expand horizontally
        for i in range(len(matrix)):
            matrix[i] += add_value_to_row(duplicate[i], t)

    duplicate = duplicate_matrix(matrix)
    
    for t in range(1, times):  # expand vertically
        matrix += add_value_to_matrix(duplicate, t)


def main():
    # inputs = standard_func.get_input_as_str('input.txt')
    inputs = standard_func.get_input_as_str('test.txt')

    matrix = parse_input_into_matrix(inputs)
    expand_matrix(matrix, 5)

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
