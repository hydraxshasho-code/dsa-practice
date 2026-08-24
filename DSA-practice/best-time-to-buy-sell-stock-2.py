class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                d=prices[i+1]-prices[i]
                profit+=d
            else:
                continue
        return profit