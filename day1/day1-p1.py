import time

def main():
    depths = get_input('input.txt')
    num_increase = 0

    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            num_increase += 1

    print(num_increase)

# Boilerplate code below

def get_input(filename):
    with open(filename) as f:
        return list(map(lambda a : int(a), list((f.read()).split("\n"))))

def print_performance(start, end):
    print('Execution time (s):', round((end - start), 3))

if __name__ == "__main__":
    perf_counter_start = time.perf_counter()
    main()
    perf_counter_end = time.perf_counter()
    print_performance(perf_counter_start, perf_counter_end)