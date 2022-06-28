class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = [0]*26
        
        for c in s:
            l[ord(c) - ord('a')] += 1
            
        #l = [i for i in l if i != 0]
        l.sort(reverse = True)
       
        c = 0
        for i in xrange(1, len(l)):
            if l[i - 1] <= l[i]:
                k = l[i] - l[i - 1]
                if l[i - 1] != 0: k += 1
                l[i] -= k
                c += k
                
                
        return c
            
            
            
                
            
        
        
        
        
        
        
            
        