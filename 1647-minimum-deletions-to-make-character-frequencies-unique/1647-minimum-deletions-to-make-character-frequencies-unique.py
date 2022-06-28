class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = [0]*26
        
        for c in s:
            l[ord(c) - ord('a')] += 1
            
        l = [i for i in l if i != 0]
        l.sort()
       
        c = 0
        for i in xrange(1, len(l)):
            k = 0
            while l[i - 1 - k] == l[i] - k and l[i] - k > 0:
                k += 1
                #print(l, l[i], k, l[i - 1 - k], l[i]- k, i -k)
            if k > 0:
                c += k
                
                
                l.insert(i - k, l[i] - k)
                
                l.pop(i)
                #print(l, len(l), i - k, l[i] - k)
        
                
                
       
            
            
        #print(l)
        return c
            
            
            
                
            
        
        
        
        
        
        
            
        