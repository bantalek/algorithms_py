from random import randint
from fibonacci_partial_sum import fibonacci_partial_sum
from fibonacci_partial_sum_naive import fibonacci_partial_sum_naive
n = int(input()) - 1
while True:
    print('testing')
    # Generate a random number between 2 and 11
    random_size = str(randint(0, 400))
    sample_input = ''
    sample_input += random_size + '\n'

    # Generate random input to fill an input line 
    for _ in range(n):
        sample_input += str(randint(0, 400)) + ' '
    
    sample_input += '\n'
    sample_input = [int(x) for x in sample_input.split()]
    print(sample_input)
    # Compare the results of both algorithms
    result1 = fibonacci_partial_sum_naive(min(sample_input), max(sample_input))
    result2 = fibonacci_partial_sum(min(sample_input), max(sample_input))


    if result1 != result2:
        print('Wrong answer %i and %i.\n' % (result1, result2))
        break
    else:
        print('OK')


# [1, 2]
# Wrong answer 4 and 2.