import time


def main():
    inputs = get_input_as_str('input.txt')
    # inputs = get_input_as_str('test.txt')
    gamma_bin = ''
    epsilon_bin = ''

    for i in range(len(inputs[0])):
        num_0 = 0
        num_1 = 0

        for row in inputs:
            if row[i] == '0':
                num_0 += 1
            else:
                num_1 += 1

        if num_0 > num_1:
            gamma_bin += '0'
            epsilon_bin += '1'
        else:
            gamma_bin += '1'
            epsilon_bin += '0'

    print(int(gamma_bin, 2) * int(epsilon_bin, 2))


# Boilerplate code below
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
    print_performance(perf_counter_start, perf_counter_end)
