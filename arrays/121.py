'''
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n==1:
            return 0
        max_diff = prices[1]-prices[0]
        min_elem = prices[0]
        
        for i in range(n):
            '''
            buy on day when prices are low
            sell on day when prices are high
            '''
            if (prices[i]-min_elem)>max_diff:
                max_diff = prices[i]-min_elem
            
            if prices[i]<min_elem:
                min_elem = prices[i]
        
        return max_diff