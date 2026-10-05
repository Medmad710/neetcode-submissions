class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a=0
        mx=nums[0]
        for i in range(len(nums)):
            a= max(a+nums[i] , nums[i])
            mx=max(mx,a)
        return mx