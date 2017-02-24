# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current  = 1
    period = []

    for _ in range(from_ - 1):
        previous, current = current, (previous + current) % 10

    sum = current
    for _ in range(to - from_):
        previous, current = current, (previous + current) % 10
        sum += current
    

    print("control", sum % 10,"current", current, "prev", previous)
    return sum % 10


print(fibonacci_partial_sum_naive(319, 382))
if __name__ == "__main__":
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))