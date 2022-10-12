class Solution:
    def combinationSum(self, Cs: List[int], T: int) -> List[List[int]]:

        Cs.sort()
        
        def get_combs(c_i, T):
            sols =[]
            for i in range(c_i, len(Cs)):
                c = Cs[i]
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
            