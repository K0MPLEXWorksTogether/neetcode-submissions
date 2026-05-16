class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            if num > 0:
                hashset.add(num)

        for i in range(1, len(nums) + 2):
            if i not in hashset:
                return i

        return max(nums) + 1 if 1 in hashset else 1