import time


def is_valid_bracket_pair(left_b, right_b):
    match left_b:
        case '(':
            if right_b == ')':
                return True
        case '[':
            if right_b == ']':
                return True
        case '{':
            if right_b == '}':
                return True
        case '<':
            if right_b == '>':
                return True
        case _:
            return False

    return False        


def is_left_bracket(bracket):
    return bracket == '(' or bracket == '[' or bracket == '{' or bracket == '<'


def get_missing_brackets(brackets):
    stack = []

    for bracket in brackets:
        if is_left_bracket(bracket):
            stack.append(bracket)
        else:
            latest_stack_bracket = stack.pop()
            if not is_valid_bracket_pair(latest_stack_bracket, bracket):
                return []

    return stack[::-1]
            

def get_bracket_score(bracket):
    match bracket:
        case '(':
            return 1
        case '[':
            return 2
        case '{':
            return 3
        case '<':
            return 4
        case _:
            return 0


def calculate_score(missing_brackets):
    score = 0

    for bracket in missing_brackets:
        score *= 5
        score += get_bracket_score(bracket)

    return score


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    score = []
    
    for input in inputs:
        missing_brackets = get_missing_brackets(input)

        if len(missing_brackets) == 0:
            continue

        score.append(calculate_score(missing_brackets))

    print(sorted(score)[len(score)//2])


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
