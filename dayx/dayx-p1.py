import time

def main():
    # inputs = get_input_as_str('input.txt')
    inputs = get_input_as_str('test.txt')
    
    # Code goes here

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
