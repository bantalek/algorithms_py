# Uses python3
def fib_list(n):
    if n == 0:
        return 0

    result = [];
    result.append(0)
    result.append(1)

    for i in range(2, n+1):
        result.append(result[i-1] + result[i-2])

    return result[n]

n = int(input())
print(fib_list(n))
