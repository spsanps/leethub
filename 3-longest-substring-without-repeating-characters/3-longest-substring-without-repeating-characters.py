class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        l = 0
        let = [-1]*256
        ans = 0
        i = 0
        for i in xrange(len(s)):
            ind = ord(s[i])
            
            #print(let[ind])
            
            
            
            if let[ind] != -1:
                l = max(let[ind] + 1, l)
            
            let[ind] = i
            
                
            #print(l, i, ans, let[ind])
            ans = max(ans, i - l + 1)
            
        return ans
           
        
        
        