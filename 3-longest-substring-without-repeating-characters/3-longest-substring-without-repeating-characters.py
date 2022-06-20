class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxl = 0
        let_pos = {}
        for i in range(len(s)):
            c = s[i]
            
            if c in let_pos and let_pos[c] != -1:
                ltemp = let_pos[c] + 1
                for c in s[l:ltemp]:
                    let_pos[c] = -1
                
                l = ltemp

            let_pos[c] = i
                
            
            d = i - l + 1
            
            
            if d > maxl: maxl = d
                
        return maxl
            
        