class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))

        # factorial[i] = i!
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i

        # Convert k to 0-based indexing
        k -= 1

        ans = []

        for remaining in range(n, 0, -1):
            block_size = factorial[remaining - 1]

            # Which unused number starts this block?
            index = k // block_size

            ans.append(str(nums.pop(index)))

            # Position within the selected block
            k %= block_size

        return "".join(ans)