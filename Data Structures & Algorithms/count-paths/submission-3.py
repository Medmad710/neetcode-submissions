
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix =  [1]*n

        for _ in range(m-1):
            for j in range(1,n):
                    matrix[j]=matrix[j]+matrix[j-1]


                
        return matrix[-1]