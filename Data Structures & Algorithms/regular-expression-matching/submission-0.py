class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i: int, j: int) -> bool:
        # If pattern is finished, string must also be finished
            if j == len(p):
                return i == len(s)

            # Check if current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Handle '*' case (look ahead in pattern)
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option 1: skip "x*"
                # Option 2: use "x*" if first character matches
                return dfs(i, j + 2) or (first_match and dfs(i + 1, j))

            # Normal case (no '*')
            return first_match and dfs(i + 1, j + 1)

        return dfs(0, 0)