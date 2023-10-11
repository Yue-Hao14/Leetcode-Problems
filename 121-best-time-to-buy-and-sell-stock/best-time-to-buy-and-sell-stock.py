class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # idea: time O(n), space O(1)
        # iterate through prices array
        # set left and right pointers
        # if left >= right, move left to right as we find a very low price at right index
        # if left < right, move right forward, update max_profit

        # code:
        left, right = 0, 1 # left = buy, right = sell
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
                right += 1
            else:
                left = right
                right = left + 1
        
        return max_profit
