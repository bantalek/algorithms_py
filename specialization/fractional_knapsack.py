# Uses python3
import sys
import queue as Q
# index_min = min(xrange(len(values)), key=values.__getitem__)
def get_optimal_value(capacity, weights, values):
    q = Q.PriorityQueue()
    v = 0.0
    e = capacity
    for weight, value in zip(weights, values):
        q.put((value/-weight, -weight, value))
    
    while not q.empty():
        i = q.get(False)
        if (e + i[1]) >= 0:
            e += i[1]
            v += round(abs(i[2]), 4)
        else:
            e = e / i[1]
            v += round(abs(e * i[2]), 4)
            break
    return v

# print(get_optimal_value(50, [50,20,50,30], [3,60,100,120]))
# print(get_optimal_value(10, [30], [500]))

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))