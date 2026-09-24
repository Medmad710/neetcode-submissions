class Solution:
    def hammingWeight(self, n: int) -> int:
        r=0
        while n>0:
            r+=n & 1
            n>>=1
        return r