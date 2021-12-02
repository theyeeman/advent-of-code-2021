# Boiler plate code that handles reading input from file and timing performance

def get_input(filename):
    with open(filename) as f:
        return list(map(lambda a : int(a), list((f.read()).split("\n"))))

def print_performance(start, end):
    print('Execution time (s):', round((end - start), 3))