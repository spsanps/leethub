class Solution:
    def __init__(self):
        super().__init__()
        self.sols = {}
        
    def climbStairs(self, n: int) -> int:
        if n == 2:
            return 2
        if n == 1:
            return 1
        if n in self.sols:
            return self.sols[n]
        sol = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.sols[n] = sol
        return sol