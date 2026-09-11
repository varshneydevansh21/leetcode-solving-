class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        row_track = [0 for _ in range(r)]
        col_track = [0 for _ in range(c)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row_track[i] = -1
                    col_track[j] = -1
        for i in range(r):
            for j in range(c):
                if row_track[i] == -1 or col_track[j] == -1:
                    matrix[i][j] = 0
