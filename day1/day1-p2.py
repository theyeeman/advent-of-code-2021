def getInput(filename):
    with open(filename) as f:
        return list(map(lambda a : int(a), list((f.read()).split("\n"))))

if __name__ == "__main__":
    depths = getInput('input.txt')
    num_increase = 0
    prev_depth = depths[0] + depths[1] + depths[2]

    for i in range(3, len(depths)):
        curr_depth = depths[i] + depths[i - 1] + depths[i - 2]
        if curr_depth > prev_depth:
            num_increase += 1
        prev_depth = curr_depth

    print(num_increase)
