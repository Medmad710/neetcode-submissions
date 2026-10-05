class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        r=[0]*len(nums)
        for i in range(len(nums)):
            r[i]= max(r[i-1]+nums[i] , nums[i])
        return max(r)