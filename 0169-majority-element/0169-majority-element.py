class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counts = defaultdict(int)
        
        curr_max_count = 0
        curr_max_n = 0
        for n in nums:
            counts[n] += 1
            
            if counts[n] > curr_max_count:
                curr_max_count = counts[n]
                curr_max_n = n
        
        return curr_max_n
                
        