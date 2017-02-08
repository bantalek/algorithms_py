# Implement the function unique_in_order which takes as argument a sequence and returns a list 
# of items without any elements with the same value next to each other and 
# preserving the original order of elements.

def unique_in_order(iterable):
    res = []
    temp = None
    for i, char in enumerate(iterable):

        if temp == char:
            continue
        else:
            temp = char
            res.append(char)
    return res