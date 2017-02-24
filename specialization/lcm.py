# Uses python3

def gcd(dividend, divisor):
    while divisor != 0:
        t = divisor
        divisor = dividend % divisor
        dividend = t

    return dividend

def lcm_naive(a, b, gcd):
    return abs(a * b) // gcd(a, b)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b, gcd))

