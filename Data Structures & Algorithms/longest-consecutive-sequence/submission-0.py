class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res=0
        for i in nums:
            l=1
            if i-1 not in nums:
                while (i+l) in nums:
                    l+=1
                res = max(l,res)
        return res       



