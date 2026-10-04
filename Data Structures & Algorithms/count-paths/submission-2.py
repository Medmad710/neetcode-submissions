import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    matrix[i][j]=1
                else:
                    matrix[i][j]=matrix[i-1][j]+matrix[i][j-1]


                
        return matrix[-1][-1]