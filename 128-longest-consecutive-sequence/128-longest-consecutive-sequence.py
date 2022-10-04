class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        
        best = 0
        
        for n in nums:
            if n - 1 not in nums: # head
                c = 1
                curr = n
                while curr + 1 in nums:
                    curr += 1
                    c += 1
                
                best = max(best, c)
        
        return best
                
        