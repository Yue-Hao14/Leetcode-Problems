class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # set 2 pointers
        # left pointer track when to buy
        # right pointer track when to sell
        # iterate through the array to find the maxProfit
            # if right > left, check if need to update maxProfit, right+1
            # if right < left, move left to right and right+1
        left, right, max_profit = 0,1,0

        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if prices[right] > prices[left]:
                max_profit = max(current_profit, max_profit)
            else:
                left = right
            right += 1

        return max_profit


