class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        count = defaultdict(int)
        for l in magazine:
            count[l] += 1
        
        for l in ransomNote:
            if count[l] == 0:
                return False
            else:
                count[l] -= 1
        
        return True
        