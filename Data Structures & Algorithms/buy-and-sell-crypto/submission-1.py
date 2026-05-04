class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0 
        mininum = float('inf')
        for price in prices:
            if price < mininum:
                mininum =  price
            profit = price - mininum
            if profit > maximum:
                maximum = profit
        return maximum
                    
