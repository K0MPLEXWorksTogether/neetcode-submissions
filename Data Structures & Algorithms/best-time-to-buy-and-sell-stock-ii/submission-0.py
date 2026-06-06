class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = math.inf
        profit = 0

        for num in prices:
            if num < smallest:
                smallest = num
            else:
                profit += (num - smallest)
                smallest = num

        return profit
