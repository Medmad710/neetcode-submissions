class Solution:
    def rob(self, nums: List[int]) -> int:
        r=[0,0,0]
        for i in range(len(nums)):
            r[0]=r[1]
            r[1]=r[2]
            r[2]=(max(r[0] + nums[i], r[1]))
        return r[2]