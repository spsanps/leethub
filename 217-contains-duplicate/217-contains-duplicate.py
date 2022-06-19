class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        prev = nums[0]
        for i in nums[1:]:
            if i == prev: return True
            prev = i 
        return False
            
            
            
        