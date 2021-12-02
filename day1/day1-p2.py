def get_input(filename):
    with open(filename) as f:
        return list(map(lambda a : int(a), list((f.read()).split("\n"))))

if __name__ == "__main__":
    depths = get_input('input.txt')
    num_increase = 0
    sliding_window_size = 3

    for i in range(0, len(depths) - sliding_window_size):
        prev_depth = 0
        curr_depth = 0

        for j in range(sliding_window_size):
            prev_depth += depths[i + j]
            curr_depth += depths[i + j + 1]
        
        if curr_depth > prev_depth:
            num_increase += 1

    print(num_increase)
