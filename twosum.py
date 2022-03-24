class Solution(object):
    def twoSum(self, nums, target):
        hash = {}
        for i,num in enumerate(nums):
            cum = target - num
            if cum in hash:
                return [hash[cum],i]
            hash[num]=i
