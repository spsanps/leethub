class Solution(object):
    def searchRange(self, Ns, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not Ns:
            return [-1, -1]
        
        l = 0
        r = len(Ns) - 1
        
        while l <= r:
            mid = (l + r)//2
            
            print(l, mid, r)
            
            if t <= Ns[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        if Ns[mid] != t and mid < len(Ns) - 1: mid += 1 
        
        l = 0
        r = len(Ns) - 1
        mid2 = (l + r)//2
               
        while l <= r:
            mid2 = (l + r)//2
            
            print(l, mid2, r)
            
            if t < Ns[mid2]:
                r = mid2 - 1
            else:
                l = mid2 + 1
                
        if Ns[mid2] != t and mid2 > 0: mid2 -= 1
                
        if Ns[mid] != t: return [-1, -1]
                
        return [mid, mid2]
        
            
            
        