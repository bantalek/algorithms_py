# Uses python3

# This program will accomplish specifying the order of applying its arithmetic
# operations using additional parentheses to maximize its value.

# The only line of the input should contain a string 𝑠 of length 2𝑛 + 1 of integers 0-9 
# where n is the number of arithmetic operations including {+,-,*} i.e. 5 − 8 + 7 × 4 − 8 + 9

def evalt(a, b, op):
    if op   == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    operands  = []
    operators = []
    for char in range(len(dataset)):
        if char % 2 == 0:
            operands.append(dataset[char])
        else:
            operators.append(dataset[char])

    n = len(operands)
    M = []

    for i in range(n):
        M.append([0 for op in operands])
        M[i][i] = int(operands[i])

    m = [Mm[:] for Mm in M]

    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            m[i][j], M[i][j] = min_max(i, j, operators, m, M)

    return max(int(M[0][n-1]), int(m[0][n-1]))

def min_max(i, j, op, m, M):
    minv = float('inf')
    maxv = -float('inf')

    for k in range(i, j):
        a    = evalt(M[i][k], M[k+1][j], op[k])
        b    = evalt(M[i][k], m[k+1][j], op[k])
        c    = evalt(m[i][k], M[k+1][j], op[k])
        d    = evalt(m[i][k], m[k+1][j], op[k])
        minv = min(minv, a,b,c,d)
        maxv = max(maxv, a,b,c,d)

    return (int(minv), int(maxv))

# print(get_maximum_value("5-8+7*4-8+9"))
# print(get_maximum_value("1+2-3*4-5"))

if __name__ == "__main__":
    print(get_maximum_value(input()))