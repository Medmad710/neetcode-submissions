class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        r=[1]*(len(nums)+1)


        for i in range(len(nums)):
            for j in range(0,i+1):
                if nums[j]<nums[i]:
                    r[i]= max(r[i],r[j]+1)
            
        return max(r)

