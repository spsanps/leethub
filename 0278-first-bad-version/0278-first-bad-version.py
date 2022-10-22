# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        
        # bs
        
        l = 1
        r = n
        
        while l < r:
            
            mid = l + (r-l)//2
        
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
                
            #print(l, r, mid)
                
            
        if not isBadVersion(r):
            r += 1
        return r
        