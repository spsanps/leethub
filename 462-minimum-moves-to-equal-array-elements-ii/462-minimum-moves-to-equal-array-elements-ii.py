class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """  
        
        nums.sort()
        
        ltar = nums[0]
        rtar = nums[-1]
        
        c = [0]*len(nums)
        
        lprev = 0
        rprev = 0
        for i in xrange(len(nums)):
            ri = len(nums) - 1 - i
            
            la = (nums[i] - ltar)*i 
            ra = (-nums[ri] + rtar)*i 
            c[i] += la + lprev
            c[ri] += ra + rprev
            
            lprev += la
            rprev += ra
                     
            ltar = nums[i]
            rtar = nums[ri]
            
            #print(nums[i], nums[ri], c)
            
        return min(c)
            
            
            
        
        
        
        
        
            
            
            
            