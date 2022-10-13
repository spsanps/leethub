class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        """        
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
        """
        
       
        tabulation = [list([0]*(amount + 1)) for i in range(len(coins) + 1)]
        """
        def print_tab():
            for i in range(len(coins) + 1):
                for j in range(amount + 1):
                    print(tabulation[i][j], end = ' ')
                print()
            print()
        """
        #print_tab()
        
        for j in range(1, amount + 1): # when amount is 0, it is okay
            tabulation[0][j] = math.inf # no solutions when not picking any coins
        
        #print_tab()
        
        for i in range(len(coins)):
            tabulation[i][0] = 0
        
        #print_tab()
        
        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                c = coins[i - 1]
                if c > j:
                    tabulation[i][j] = tabulation[i - 1][j]
                else:
                    tabulation[i][j] = min(1 + tabulation[i][j - c], 0 + tabulation[i - 1][j])
                
                #print_tab()

        
        ans = tabulation[len(coins)][amount] 
        
        return ans if ans < math.inf else -1