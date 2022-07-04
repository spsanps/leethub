class Solution(object):
    def candy(self, r):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        k = list(r)
        
        #for i in xrange(len(r)):
        #    if ((i == 0 or r[i - 1] == r[i]) and (i == len(r) - 1 or r[i] == r[i + 1])):
        #        r[i] = 0
        
        #r = list(k)
        #print(r)
               
        r_is = sorted(zip(r, range(len(r))), key = lambda x : x[0])
            
    
        for v, r_i in r_is:
            b = r[r_i]
           
            #print(b)
            if (r_i == 0):
                m = 0
            else:
                a = r[r_i - 1]
                if (a >= b or k[r_i - 1] == k[r_i]):
                    m = 0
                else:
                    m = a + 1
                
            if (r_i == len(r) - 1):
                n = 0
            else:
                c = r[r_i + 1]
                if (c >= b or k[r_i + 1] == k[r_i]):
                    n = 0
                else:
                    n = c + 1

            #print(r)
            
            #print(m, n)
            
            r[r_i] = max(m, n)
            
            #print(r)
            
        return len(r) + sum(r)
            
            
        