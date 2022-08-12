class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero, one = 0, 0
        
        for n in nums:
            if n == 0:
                nums[zero] = 0
                zero += 1
            elif n == 1:
                one += 1
                
        for i in range(zero, zero + one):
            nums[i] = 1
        
        for i in range(zero + one, len(nums)):
            nums[i] = 2
        
                
        
        
        