class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        if len(nums) <= 3: return max(nums)
        
        prev2, prev1 = 0, nums[0]
        
        prev22, prev12 = 0, nums[1]
        
        for i in range(1, len(nums) - 1):
            
            res_i1 = max(prev2 + nums[i], prev1)
            
            res_i2 = max(prev22 + nums[i + 1], prev12)
            
            prev2, prev1 = prev1, res_i1
            
            prev22, prev12 = prev12, res_i2
            
            #print(res_i1, res_i2)
            
            print(prev2, prev1)
            
        return max(res_i1, res_i2)
            
        