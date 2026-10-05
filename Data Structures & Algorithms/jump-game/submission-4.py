class Solution:
    def canJump(self, nums: List[int]) -> bool:
        c=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if c-i <= nums[i]:
                c=i
        if c==0:
            return True
        else: return False