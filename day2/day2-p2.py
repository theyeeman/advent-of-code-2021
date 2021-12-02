import time

def main():
    # commands = get_input_as_str('test.txt')
    commands = get_input_as_str('input.txt')
    h_pos = 0
    depth = 0
    aim = 0
    
    for command in commands:
        direction, distance = command.split(' ')[0], int(command.split(' ')[1])

        match direction:
            case 'forward':
                h_pos += distance
                depth += aim * distance
            case 'up':
                aim -= distance
            case 'down':
                aim += distance
            case _:
                print('invalid')
        
    print(h_pos * depth)

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
