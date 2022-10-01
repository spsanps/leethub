class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '0':
            return 0
        if len(s) == 1:
            return 1
        


        prev_comb_single = 1 if s[0] != '0' else 0
        prev_comb_double = 0
        prev_c  = int(s[0])
        prev_prev_comb_total = 1
        
        
        for i in range(1, len(s)):
            c = int(s[i])
            condition_double = (prev_c > 0 and prev_c <= 2) and \
                            (prev_c <= 1 or c <= 6)
        
            curr_comb_single = 1 if c != 0 else 0
            curr_comb_single = (prev_comb_double + prev_comb_single)*curr_comb_single

            curr_comb_double = 1 if condition_double else 0
            curr_comb_double = prev_prev_comb_total*curr_comb_double
            
            #print(curr_comb_single, curr_comb_double, prev_prev_comb_total)
            
            prev_prev_comb_total = prev_comb_single + prev_comb_double
            
            prev_comb_single = curr_comb_single
            prev_comb_double = curr_comb_double
            prev_c = c
            
            
            
        return curr_comb_double + curr_comb_single
        