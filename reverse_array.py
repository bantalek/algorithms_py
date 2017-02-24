
def reverse_array(arr):

    string = ''
    for n in arr:
        string = "%d " % n + string
    print(string)

if __name__ == "__main__":
    arr = [int(n) for n in input().strip().split(' ')]
    reverse_array(arr)