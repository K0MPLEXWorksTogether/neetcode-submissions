class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = []
        suffix = []

        prod = 1
        for num in nums:
            prod *= num
            prefix.append(prod)

        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod *= nums[i]
            suffix.append(prod)
        suffix.reverse()

        for i in range(len(nums)):
            if i == 0:
                result.append(suffix[1])
            elif i == len(nums) - 1:
                result.append(prefix[i - 1])
            else:
                result.append(prefix[i - 1] * suffix[i + 1])

        return result