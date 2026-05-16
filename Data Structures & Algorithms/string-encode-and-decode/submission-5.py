class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += f"{len(string)}#{string}"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0 
        decoded = []
        while(i < len(s)):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            decoded.append(s[i : i + length])
            i += length
        
        return decoded
