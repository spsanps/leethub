class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        
        l_dict = {}
        
        count = 0
        for c in s:
            if c in l_dict:
                l_dict[c] = not l_dict[c]
                if l_dict[c] is False:
                    count += 2
            else:
                l_dict[c] = True
                
            #print(l_dict)
                
        for l in l_dict:
            if l_dict[l] is True:
                count += 1
                break
        
        return count
        
                    
                    
        