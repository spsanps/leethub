class Solution:
    def combinationSum(self, Cs: List[int], T: int) -> List[List[int]]:

        Cs.sort()
        
        def get_combs(c_i, T):
            sols =[]
            #print('T:', T)
            
            #if T < 0: return []
            #if T == 0: return [[]]
            
            for i in range(c_i, len(Cs)):
                c = Cs[i]
                #print(c)
                if c < T:
                    s = get_combs(i, T - c)          
                    s = [list(a + [c]) for a in s]
                    sols.extend(s)
                elif c > T:
                    break
                else:    
                    sols.append([c])
                    break
            return sols
        
        return get_combs(0, T)
            