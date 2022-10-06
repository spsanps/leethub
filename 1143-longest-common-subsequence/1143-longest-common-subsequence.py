class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(m+1) for _ in range(n + 1)]
        
        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                
                if c1 == c2:
                    dp[j + 1][i + 1] = dp[j][i] + 1
                else:
                    dp[j + 1][i + 1] = max(dp[j][i + 1], dp[j + 1][i])
        
        return dp[n][m]


        