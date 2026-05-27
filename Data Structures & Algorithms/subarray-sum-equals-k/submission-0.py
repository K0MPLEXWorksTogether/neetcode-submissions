class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        prefixSum = 0
        count = 0

        for num in nums:
            prefixSum += num

            if (prefixSum - k) in hashmap:
                count += hashmap[prefixSum - k]

            hashmap[prefixSum] = hashmap.get(prefixSum, 0) + 1

        return count
