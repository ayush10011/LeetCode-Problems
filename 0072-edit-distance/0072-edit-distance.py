class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Make word2 the shorter string to reduce memory usage
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        n = len(word2)

        # prev[j] = answer for converting processed part of word1
        # into word2[:j]
        prev = list(range(n + 1))

        for i in range(1, len(word1) + 1):
            curr = [i] + [0] * n

            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(
                        prev[j],      # delete
                        curr[j - 1],  # insert
                        prev[j - 1]   # replace
                    )

            prev = curr

        return prev[n]