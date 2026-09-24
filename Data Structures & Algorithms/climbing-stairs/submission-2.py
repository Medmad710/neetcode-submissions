class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0]*n
        res[n-1]=1
        res[n-2]=2
        if n in [1,2]:
            return n
        for i in range(n-3,-1,-1):
            res[i] = res[i+1]+res[i+2]
        return res[0]


            
