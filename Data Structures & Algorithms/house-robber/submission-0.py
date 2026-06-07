class Solution:
    def rob(self, nums: List[int]) -> int:
        def backtrack(i, memo = {}):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            else:
                money = nums[i]
                memo[i] = max(money + backtrack(i + 2), backtrack(i + 1))
                return memo[i]

        return backtrack(0, {})