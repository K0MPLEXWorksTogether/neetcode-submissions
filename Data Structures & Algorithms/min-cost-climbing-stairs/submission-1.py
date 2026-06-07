class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def backtrack(i, memo=None):
            if memo is None:
                memo = {}

            if i >= len(cost):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = min(
                cost[i] + backtrack(i + 1, memo),
                cost[i] + backtrack(i + 2, memo)
            )

            return memo[i]
        return min(backtrack(0), backtrack(1))