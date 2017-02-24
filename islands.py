class Matrix: 
    def __init__(self, rows, cols, matrix):
        self.g = matrix
        self.m = rows
        self.n = cols
    
    def check_move(self, i, j, visited):
        # checking a move involves confirming i and j are in bounds of matrix and
        # checking to make sure the position has not been visited and
        # and checking the positions value is of interest aka 1
        
        if (0 <= i < n             and
            0 <= j < m             and
            not visited[i][j]      and
            self.g[i][j] == 1):
            return True

    def DFS(self, i, j, visited):
        # create an array of integers 0, 1, -1 that will represent the coordinates of all neighbors to any one position and
        # mark the position as visited and
        # for all possible moves to a neighbor of the position, check if the move is valid and
        # DFS the neighbor if it is a valid move

        row_n = [1,1,1,0,0,-1,-1,-1]
        col_n = [0,1,-1,1,-1,0,1,-1]

        visited[i][j] = True
        
        for k in range(8):
            if self.check_move(i + row_n[k], j + col_n[k], visited):
                self.DFS(i + row_n[k], j + col_n[k], visited)


    def count_islands(self):
        # generate a visited matrix len m x n with initial falsey values and
        # for every position in the matrix, check if the move is safe and
        # DFS from the position to check all neighbors for relevant connection and
        # skip positions that are not relevant or have been visited

        count = 0
        visited = [[False for j in range(self.m)] for i in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.m):
                if self.check_move(i, j, visited):
                    self.DFS(i, j, visited)
                    count += 1
                    
        return count

matrix = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
]

n = len(matrix[0])
m = len(matrix)

g = Matrix(m, n, matrix)
print(g.count_islands())