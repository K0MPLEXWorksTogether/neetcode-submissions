class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set()
        for num in nums:
            hash_set.add(num)

        max_count = 0
        for num in nums:
            count = 1
            if num - 1 not in hash_set:
                start = num + 1
                while start in hash_set:
                    count += 1
                    start += 1
                
            max_count = max(max_count, count)

        return max_count