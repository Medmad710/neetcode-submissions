class Solution:
    def reverseBits(self, n: int) -> int:
        c=0
        for _ in range(32):
            c=c<<1
            if n&1:
                c+=1
            n=n>>1
            
        return c 
