class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ps = [1 for i in range(len(nums))]
       
        
        def left_prod(ind):
            if ind < 0: return 1
            ps[ind] = left_prod(ind - 1)
            return ps[ind]*nums[ind]
                
        
        def right_prod(ind):
            if ind > len(nums) - 1: return 1 
            p = right_prod(ind + 1)
            ps[ind] = ps[ind]*p
            return p*nums[ind]
        
        left_prod(len(nums) - 1)
        right_prod(0)
        
        return ps
            
            

            
        