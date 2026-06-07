class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {}

        def helper(state):
            state = tuple(state)

            if state in memo:
                return memo[state]

            if not state:
                return 0

            max_coins = 0

            for i in range(len(state)):
                left = state[i - 1] if i > 0 else 1
                right = state[i + 1] if i < len(state) - 1 else 1

                gain = left * state[i] * right

                new_state = state[:i] + state[i+1:]

                total = gain + helper(new_state)

                max_coins = max(max_coins, total)

            memo[state] = max_coins
            return max_coins

        return helper(nums)