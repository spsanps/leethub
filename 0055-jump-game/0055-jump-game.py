class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        """i_n = list(enumerate(nums))

        curr_end = nums[0] # + 0
        curr_start = 0
        
        while True:
                        
            print(curr_start, curr_end)
            
            if curr_end >= len(nums) - 1:
                return True
            
            end_i, end_n = max(i_n[curr_start:curr_end], key=lambda t: t[0] + t[1])
                        
            new_start = end_i + end_n
            
            print(end_i)
            
            if new_start >= len(nums) - 1:
                return True
            
            if new_start <= curr_end:
                return False
            
            curr_start = new_start
            
            curr_end = nums[new_start] + new_start"""
        
        m = nums[0]
        
        for i, n in enumerate(nums):

            if i + n > m:
                m = i + n
            
            if m >= len(nums) - 1:
                return True
            elif i == m:
                return False

            
        return True 