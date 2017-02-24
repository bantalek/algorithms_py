# Uses python3
import sys

def fibonacci_sum(n):
    if n <= 1:
        return n

    period   = [0,1]
    previous = 0
    current  = 1

    for _ in range(n - 1):
        if len(period) > 2 and previous == 0 and current == 1:
            x = len(period) - 2
            y = n // x
            z = n % x
            print('sum', period, x, y, z)
            return sum([sum(period[:x]) % 10 * y, sum(period[:z+1]) % 10]) % 10

        else:
            previous, current = current, (previous + current) % 10
            period.append(current)
    return sum(period) % 10

# print(fibonacci_sum(1000))

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))