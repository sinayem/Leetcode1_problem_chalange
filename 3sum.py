class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,val in enumerate(nums):
            if i>0 and nums[i-1]==val:  # remove first layer duplicacy 
                continue
            l,r = i+1, len(nums)-1
            
            while l<r:
                if val + nums[l] + nums[r] >0:
                    r -= 1
                elif val + nums[l] + nums[r] <0:
                    l += 1
                else:
                    res.append([val,nums[l],nums[r]])
                    l +=1
                    while nums[l]==nums[l-1] and l<r:  # remove duplicacy
                        l+=1
        return res
            
  # [-4,-1,-1,-1,0,1,2]
  #https://leetcode.com/problems/3sum/
