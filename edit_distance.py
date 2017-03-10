# Uses python3

def insert(m,i,j):
    if (i < 0 or j < 0): return float('nan')
    return m[i][j-1] + 1
def delete(m,i,j): 
    if (i < 0 or j < 0): return float('nan')
    return m[i-1][j] + 1
def mismatch(m,i,j): 
    if (i < 0 or j < 0): return float('nan')
    return m[i-1][j-1] + 1
def match(m,i,j): 
    if (i < 0 or j < 0): return float('nan')
    return m[i-1][j-1]


"""
The edit distance between two strings is the
minimum number of operations to transform one string into another. It is a measure
of similarity of two strings. Edit distance has applications in computational
biology, natural language processing, and spell checking. The goal of this 
program is to compute the edit distance between two strings.
"""

def edit_distance(a, b):

    ly = len(a) + 1
    lx = len(b) + 1
    m =  [[0 for x in range(lx)] for y in range(ly)]

    count = 0
    for i in range(max(lx, ly)):
        if i < lx:
            m[0][i] = count
        if i < ly:
            m[i][0] = count
        count += 1

    for i in range(1,ly):
        for j in range(1,lx):
            if(a[i-1] == b[j-1]):
                m[i][j] = min(insert(m,i,j), delete(m,i,j), match(m,i,j))
            else: 
                m[i][j] = min(insert(m,i,j), delete(m,i,j), mismatch(m,i,j))
    return(m[ly-1][lx-1])



if __name__ == "__main__":
    print(edit_distance(input(), input()))
