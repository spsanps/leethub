class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        dp_dict = {}
        
        def dp(c_i, amount):
            
            if c_i >= len(coins):
                return math.inf
            
            if amount < 0:
                return math.inf
            elif amount == 0:
                return 0
            
            if (c_i, amount) in dp_dict:
                return dp_dict[(c_i, amount)]
            
            ans = min(1 + dp(c_i, amount - coins[c_i]), \
                       0 + dp(c_i + 1, amount) )
            
            dp_dict[(c_i, amount)] = ans 
            
            return ans
                
        ans = dp(0, amount)
        return ans if ans < math.inf else -1
                