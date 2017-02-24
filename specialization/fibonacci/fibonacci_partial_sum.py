# Uses python3
import sys

def fibonacci_partial_sum(from_, to, mod=10):
    if to <= 1:
        return to
    
    N = to - from_
    n = from_ - 1 if from_ > 0 else 0
    to = to - 1 if from_ > 0 else to

    previous = 0
    current  = 1

    period      = []
    cycle_count = 60
    cycle = (n) % cycle_count
    
    while len(period) < 60:
        previous, current = current, (previous + current) % mod
        period.append(current)    
    
    if from_ == 0:
        cycles           = N // cycle_count
        cycles_remainder = N % cycle_count

        current          += sum(period) * cycles
        current          += sum(period[:cycles_remainder])

        return current % mod

    else: 
        N                -= (cycle_count - cycle)
        cycles           = N // cycle_count
        cycles_remainder = N % cycle_count

        current          = sum(period[cycle - 1:])
        current          += sum(period) * cycles
        current          += sum(period[:cycles_remainder])

        return current % mod

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to, 10))