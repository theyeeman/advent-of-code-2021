import time

# Constants
MARKED = -1
WIN = -5


def has_line(board):
    for row in board:
        if sum(row) == WIN:
            return True

    # Transpose board
    t_board = zip(*board)

    for row in t_board:
        if sum(row) == WIN:
            return True

    return False


def mark_board(board, num):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == num:
                board[row][col] = MARKED


def get_bingo_boards(l):
    board_list = []
    curr_board = []

    for row in l[2:]:
        if row == '':
            board_list.append(curr_board.copy())
            curr_board.clear()

        else:
            curr_board.append(_format_bingo_row(row))

    board_list.append(curr_board.copy())  # Append last remaining board
    return board_list


def _format_bingo_row(row):
    # Takes in string like '22 13 17 11  0' or ' 8  2 23  4 24' and returns list of numbers 
    return list(map(lambda a : int(a), [x for x in row.split(' ') if x != '']))


def get_bingo_nums(l):
    return list(map(lambda a : int(a), l[0].split(',')))


def print_bingo_board(board):
    for row in board:
        print(row)


def get_board_score(board, win_num):
    score = 0

    for row in board:
        for num in row:
            if num != -1:
                score += num

    return score * win_num


def main():
    inputs = standard_func.get_input_as_str('input.txt')
    # inputs = standard_func.get_input_as_str('test.txt')
    
    bingo_nums = get_bingo_nums(inputs)
    bingo_boards = get_bingo_boards(inputs)

    for num in bingo_nums:
        for board in bingo_boards:
            mark_board(board, num)

        i = 0
        while i < len(bingo_boards):
            if has_line(bingo_boards[i]):
                last_popped = bingo_boards[i].copy()
                last_num_to_pop = num
                bingo_boards.pop(i)
            else:
                i += 1

    print(get_board_score(last_popped, last_num_to_pop))


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
