class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        count = {}
     
        for l in s:
            if l in count:
                count[l] += 1
            else:
                count[l] = 1
        
        #print(count)
        
        for l in t:
            if l in count:
                if count[l] == 0:
                    return False
                count[l] -= 1
            else:
                return False
            
        #print(count)
        
        for l in count:
            if count[l] != 0:
                return False

        return True
        