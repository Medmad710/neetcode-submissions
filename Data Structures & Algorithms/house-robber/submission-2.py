class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b=0,0
        r=0
        for i in range(len(nums)):
            a=b
            b=r
            r=(max(a + nums[i], b))
        return r