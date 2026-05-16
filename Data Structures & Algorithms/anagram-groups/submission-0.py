class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()

        for string in strs:
            sortedStr = "".join(sorted(string))
            if hashmap.get(sortedStr):
                hashmap[sortedStr].append(string)
            else:
                hashmap[sortedStr] = [string]
        
        result = []
        for key in hashmap:
            result.append(hashmap[key])

        return result

           