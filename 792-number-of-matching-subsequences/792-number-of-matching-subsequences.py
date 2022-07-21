class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        ind_map = {}
        for i in range(len(s)):
            if s[i] in ind_map:
                ind_map[s[i]].append(i)
            else:
                ind_map[s[i]] = [i]
        
        count = 0
        
        for w in words:
            prev_ind = -1
            yes = True
            for c in w:
                
                if c not in ind_map:
                    yes = False
                    break

                for i in ind_map[c]:
                    if i > prev_ind:
                        prev_ind = i
                        break
                else:
                    yes = False
                    break
            
            if yes: count +=1
                
        return count

                            
                
            
            
        