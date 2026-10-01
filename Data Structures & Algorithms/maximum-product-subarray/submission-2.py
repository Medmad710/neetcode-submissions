class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn,mx=1,1
        r=nums[0]
        for i in nums:
            mn,mx= min([i*mn,mx*i ,i]),max([i,mx*i,mn*i])
            r=max(mn,mx,r)
        return r
