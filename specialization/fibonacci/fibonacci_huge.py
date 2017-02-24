# Uses python3
import sys

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    period = [0, 1]

    if m >= 2:
        for _ in range(n - 1):
            if len(period) > 2 and previous == 0 and current == 1:
                x = len(period) - 2
                y = n % x
                return period[y]
            else:
                previous, current = current, (previous + current) % m
                period.append(current)
        return current
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
