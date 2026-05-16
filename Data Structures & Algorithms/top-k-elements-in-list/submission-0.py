class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        freq_list = []
        for key in hashmap:
            freq_list.append(hashmap[key])

        freq_list.sort()
        result = []
        kth_freq = freq_list[len(freq_list) - k]
        for key in hashmap:
            if hashmap[key] >= kth_freq:
                result.append(key)

        return result

        
