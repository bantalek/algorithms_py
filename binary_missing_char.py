# Find the missing letter

# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Example:

# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'

def find_missing_letter(chars):
    expect = ord(chars[0])
    for alpha in chars:
        if expect != ord(alpha):
            return chr(ord(alpha)-1)
        expect += 1
        continue

print(find_missing_letter(['a','b','c','d','f']))