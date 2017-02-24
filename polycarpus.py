import itertools
import functools


numbers = raw_input("Your list")

def purify(numbers):
    pure = []
    numb = [int(i) for i in numbers.split()]
    for l in numb:
        if l%2 == 0:
            pure.append(l)
        else:
            continue
    return pure


print(purify(numbers))

