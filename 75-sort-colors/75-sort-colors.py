class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        from collections import Counter
        
        c = Counter(nums)
        
        for i in range(c[0]):
            nums[i] = 0
            
        for i in range(c[0], c[0] + c[1]):
            nums[i] = 1
            
            
        for i in range(c[0] + c[1], len(nums)):
            nums[i] = 2
        
        
        