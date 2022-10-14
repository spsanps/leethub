class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        p = sum(nums)
        
        if p%2 == 1: return False
        
        t = p//2
        
        dp_mem = [True] + [False]*t
        
        for n in nums:
            for i in range(t - n, -1, -1):
                dp_mem[i + n] = dp_mem[i + n] or dp_mem[i]
                #print(dp_mem)
                
        return dp_mem[t]
        """
        lsum, rsum = 0, 0
        for n in nums:
            if lsum > rsum:
                rsum += n
            else:
                lsum += n
        
        lsum, rsum = (lsum, rsum) if lsum > rsum else (rsum, lsum)
        
        diff = lsum - rsum"""
        
        
        
        
        
        