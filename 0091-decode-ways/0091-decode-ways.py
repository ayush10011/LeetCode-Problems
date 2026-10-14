class Solution:
    def numDecodings(self, s: str) -> int:
        prev2, prev1 = 1, int(s[0] != '0')

        for i in range(1, len(s)):
            curr = 0

            if s[i] != '0':
                curr += prev1

            if 10 <= int(s[i-1:i+1]) <= 26:
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1