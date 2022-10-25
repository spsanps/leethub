class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        dp_map = {}
        
        def dp(i):
            
            if i in dp_map: return dp_map[i]
            
            if i >= len(nums): return 0
            
            res = max(nums[i] + dp(i + 2), dp(i + 1))
            
            dp_map[i] = res
            
            return res
        
        return dp(0)
        