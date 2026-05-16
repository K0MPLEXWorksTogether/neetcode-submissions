class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in hashmap:
                hashmap[sorted_string].append(string)
            else:
                hashmap[sorted_string] = []
                hashmap[sorted_string].append(string)

        result = []
        for value in hashmap.values():
            result.append(value)
        return result