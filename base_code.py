import time
import common_func

def main():
    input = common_func.get_input('input.txt')
    # Main code goes here

if __name__ == "__main__":
    perf_counter_start = time.perf_counter()
    main()
    perf_counter_end = time.perf_counter()
    common_func.print_performance(perf_counter_start, perf_counter_end)