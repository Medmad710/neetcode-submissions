class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b=0,0
        r=[0,0]
        for i in range(len(nums)):
            b=r[-1]
            a=r[-2]
            r.append(max(a + nums[i], b))
        return r[-1]