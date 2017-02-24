# Uses python3

def gcd(dividend, divisor):
    while divisor != 0:
        t = divisor
        divisor = dividend % divisor
        dividend = t
    return dividend

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
