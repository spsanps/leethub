class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        #find pivot:
        
        
        
        l, u = 0, len(nums) -  1
        
        #m = 0
        
        if nums[0] <= nums[-1]:
            m = 0
        else:
            while l < u:
                m = (l + u)/2
                #print("m", m)
                if nums[m] < nums[0]:
                    u = m 
                else:
                    l = m + 1
                
        #print(l)
        m = l
        
        l, u = 0, len(nums) -  1
        while l <= u:
            m2 = (l + u)/2
            #print m2
            #print m2 + m
            if nums[(m2 + m)%len(nums)] == target:
                return (m2 + m)%len(nums)
            elif nums[(m2 + m)%len(nums)] < target:
                l = m2 + 1
            else:
                u = m2 - 1
            
        return -1