class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #ret = 5
        
        #map_v = {"a": 0, "e": 1, "i": 2, "0": 3, "u": 4}
        
        nmap = {0: [1], 
                1: [0, 2],
                2: [0, 1, 3, 4],
                3: [2, 4],
                4: [0]}
        
        mem = [1, 1, 1, 1, 1]
        new_mem = [0, 0, 0, 0, 0]
        
        for i in xrange(1, n):
            new_mem = [0]*5
            for j in xrange(5):
                for k in nmap[j]:
                        new_mem[k] += mem[j]
                        new_mem[k] %= (1000000000 + 7)
            mem = list(new_mem)
            #print(mem)
                    
        ret = sum(mem)
            
        return ret%(1000000000 + 7)
            
        
       
        
        