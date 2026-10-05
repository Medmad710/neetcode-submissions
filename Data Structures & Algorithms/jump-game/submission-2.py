class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r=[0]*len(nums)
        r[0]=nums[0]
        if len(nums)==1:
            return True
        for i in range(len(nums)):
            if r[i]==0:
                return False
            r[1+i:i+1+nums[i]]=[1]*nums[i]
        return True