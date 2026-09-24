class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  
        for t in range(len(nums)):
            if t>0 and nums[t]== nums[t-1]:
                continue
            l=t+1
            r=len(nums)-1
            while l<r :
                while l>t+1 and nums[l]== nums[l-1]:
                    l+=1
                while r<len(nums)-1 and nums[r]== nums[r+1]:
                    r-=1
                while l < r and nums[l]+nums[r]<-nums[t]:
                    l+=1
                while r>l and nums[l]+nums[r]>-nums[t] :
                    r-=1
                if l<r and nums[l]+nums[r]+nums[t]==0:
                    res.append([nums[l],nums[r],nums[t]])
                    l+=1
                    r-=1
                
        return res