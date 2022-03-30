class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        a=[]
        x=0
        for i in nums:
            if i==1:
                x+=1
            elif i==0:
                y=x
                a.append(y)
                x=0
        a.append(x)
        return max(a)
        
        
            
  #https://leetcode.com/problems/max-consecutive-ones/
