class Solution(object):
    def makesquare(self, ms):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        
                
        sel = 'F'*15
        
        tsum = sum(ms)
        
        if tsum%4 != 0: return False
        
        tar = tsum/4
        
        dp_mem = {}
        
        def rec(sel, sides, curr_sum):
            
            if curr_sum > 0 and curr_sum % tar == 0:
                sides += 1
            
            if sides == 3: return True
            
            if (sel, sides) in dp_mem:
                return dp_mem[(sel, sides)]
            
            rem = -curr_sum%tar
            if rem == 0: rem = tar
            
            #print(rem)
            #ans = False
            nsel = sel
            for i in range(len(ms)):
                if sel[i] == 'T': continue
                if ms[i] <= rem:
                    nsel = sel[:i] + 'T' + sel[i + 1:]
                    
                    #print(nsel)
                    
                    if rec(nsel, sides, curr_sum + ms[i]):
                        return True
                        break
                #print(dp_mem)
            
                dp_mem[(nsel, sides)] = False
            return False
        
        return rec(sel, 0, 0)
            
        
                    
            
        
        
            
        
        
        
        
        
        
        
        