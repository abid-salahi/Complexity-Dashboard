import sys


def calc_fib(n: int):
    if n == 0:
        return n

    previous = 1
    previous_previous = 0

    while n > 1:
        curr = previous + previous_previous
        previous_previous = previous
        previous = curr
        n -= 1

    return previous


def all_fib(limit: int):
    all_fibs = []
    while limit > 0:
        all_fibs.append(calc_fib(limit - 1))
        limit -= 1
    return all_fibs


if __name__ == "__main__":
    all_fib(3000 + int(sys.argv[1]))
    print("done!")
