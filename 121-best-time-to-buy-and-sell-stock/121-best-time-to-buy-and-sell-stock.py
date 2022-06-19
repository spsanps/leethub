class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_sofar = prices[0]
        for price in prices:
            if price - min_sofar > max_profit:
                max_profit = price - min_sofar
            if price < min_sofar:
                min_sofar = price
        return max_profit
            
        