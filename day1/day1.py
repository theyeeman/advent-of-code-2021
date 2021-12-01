def getInput(filename):
    with open(filename) as f:
        return list(map(lambda a : int(a), list((f.read()).split("\n"))))

if __name__ == "__main__":
    print(getInput('test.txt'))