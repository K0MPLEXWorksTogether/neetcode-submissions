class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for key, value in hashmap.items():
            if value > 1:
                return True

        return False