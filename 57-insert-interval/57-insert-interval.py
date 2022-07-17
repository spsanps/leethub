class Solution(object):
    def insert(self, Is, nI):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        ret = []
        na, nb = nI
        
        start = done = False
        for a, b in Is:
            if not start:
                if not done and na <= b: 
                    new_a = min(a, na)
                    start = True
                else:
                    ret.append([a, b])
            
            if start:
                if nb < a:
                    ret.append([new_a, nb])
                    ret.append([a, b])
                    done = True
                    start = False
                else:
                    if nb < b: nb = b
                        
        if not done:
            if start:
                ret.append([new_a, nb])
            else:
                ret.append(nI)
        
        return ret
            
                
        