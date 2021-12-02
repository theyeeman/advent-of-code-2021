def get_input(filename):
    with open(filename) as f:
        return list(map(lambda a : int(a), list((f.read()).split("\n"))))

if __name__ == "__main__":
    depths = get_input('input.txt')
    num_increase = 0

    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            num_increase += 1

    print(num_increase)
