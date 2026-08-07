class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = float('inf')
        profit = 0 

        for each in prices:
            mp = min(mp, each)
            profit = max(profit, each - mp)

        return profit