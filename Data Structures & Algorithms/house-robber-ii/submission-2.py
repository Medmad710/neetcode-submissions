class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b,r = 0,0,0
        r2=0
        for i in nums[:-1]:
            a=b
            b=r
            r=max(a+i,b)
        a,b = 0,0
        for j in nums[1:]:
            a=b
            b=r2
            r2=max(a+j,b)
        return max(r,r2,nums[0])