class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #inv, index
        m = {}
        
        
        for i in range(len(nums)):
            
            n = nums[i]
            inv = target - n
            
            
            if n in m:
                return [m[n], i]
            else:
                m[inv] = i
                
        