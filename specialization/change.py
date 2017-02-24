# Uses python3
import sys

def get_change(m):
    #write your code here
    d = [ 1, 5, 10 ]
    n = 0
    while len(d) > 0:
        u = d.pop()
        n += m // u
        m = m % u
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
