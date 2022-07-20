class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        
        hset = set(nums)
        
        f_pos = len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                f_pos = i
                break

        if f_pos == 0: return []
             
        max_p = nums[-1]
        min_n = nums[0]
        
        # p_sums < -min_n
        
        sol = []
    
        #print(f_pos, max_p, min_n)
        #print(nums)
        
        prev_n = None
        prev_m = None
        
        for i in range(f_pos, len(nums)):
            
            if nums[i] > -min_n: break
            if nums[i] == prev_n: continue
            else: prev_n = nums[i]
            
            prev_m = None
            
            for j in range(i + 1, len(nums)):
            
                if nums[j] + nums[i] > -min_n: break
                if nums[j] == prev_m: continue
                else: prev_m = nums[j]
                
                s = nums[j] + nums[i]
                
                #print(-s, nums[i], nums[j])
                
                if -s in hset: sol.append([-s, nums[i], nums[j]])
        
        for i in range(f_pos - 1, -1, -1):
            #print(i, nums[i])
            
            if -nums[i] > max_p: break
            if nums[i] == prev_n: continue
            else: prev_n = nums[i]
            
            prev_m = None
            
            for j in range(i - 1, -1, -1):
                               
                if -nums[j] - nums[i] > max_p: break
                
                if nums[j] == prev_m: continue
                else:
                    prev_m = nums[j]
                    
                
                s = nums[j] + nums[i]
                
                if s == 0:
                    if j > 0 and nums[j - 1] == 0:
                        sol.append([0, 0, 0])
                        continue
                    else:
                        continue
                        
                
                #print(-s, nums[i], nums[j])
                
                if -s in hset: sol.append([nums[j], nums[i], -s])
                
        
        return sol
        
        
            
        
        