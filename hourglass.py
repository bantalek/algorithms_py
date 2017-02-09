
# Given a  2D Array, :

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

# We define an hourglass in A to be a subset of values with indices falling in this pattern in 's graphical representation:

# a b c
#   d
# e f g
# There are  hourglasses in A , and an hourglass sum is the sum of an hourglass' values.

# Task 
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.

# Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

# Input Format

# There are  lines of input, where each line contains 6 space-separated integers describing 2D Array ; 
# every value in  will be in the inclusive range of  to .



# Output Format

# Print the largest (maximum) hourglass sum found in .


input_one = [
[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 9, 2, -4, -4, 0],
[0, 0, 0, -2, 0, 0,],
[0, 0, -1, -2, -4, 0]]

input_two = [[-1, -1, 0, -9, -2, -2],
[-2, -1, -6, -8, -2, -5],
[-1, -1, -1, -2, -3, -4],
[-1, -9, -2, -4, -4, -5],
[-7, -3, -3, -2, -9, -9],
[-1, -3, -1, -2, -4, -5]]


def find_hour_glass(matrix):
    # while pointer1 is less than arr.length - 3 and pointer2 is less than arr[pointer1]. length - 3
    # sum array integers at pointer 1 to pointer 1 + 2 for arr[pointer1][pointer2:pointer2+3] and arr[pointer1 + 2][pointer2:pointer2+3]
    # sum array integer at arr[pointer1 + 1]
    maximum = None
    hourglass = [[],[],[]]
    a = 0

    while a < len(matrix) - 2:
        b = 0
        while b < len(matrix[0]) - 2:
            hourglass[0] = matrix[a][b:b+3]
            hourglass[2] = matrix[a+2][b:b+3]
            hourglass[1] = matrix[a+1][b+1:b+2]

            result = sum([sum(glasses) for glasses in hourglass])

            if result > maximum:
                maximum = result
            elif maximum == None:
                maximum = result
            b += 1
        a += 1
    print(maximum)

find_hour_glass(input_one)
find_hour_glass(input_two)



