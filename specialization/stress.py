from random import randint
from ex1 import max_pair_wise_fast
from ex1_slow  import max_pair_wise
n = int(input())
while True:
    print('testing')
    # Generate a random number between 2 and 11
    random_size = str(randint(2, 11))
    sample_input = ''
    sample_input += random_size + '\n'

    # Generate random input to fill an input line 
    for _ in range(n):
        sample_input += str(randint(0, 100000)) + ' '
    
    sample_input += '\n'
    sample_input = [int(x) for x in sample_input.split()]
    print(sample_input)
    # Compare the results of both algorithms
    result1 = max_pair_wise_fast(sample_input)
    result2 = max_pair_wise(sample_input)

    if result1 != result2:
        print('Wrong answer %i and %i.\n' % (result1, result2))
        break
    else:
        print('OK')


