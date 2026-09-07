class Solution:
    def climbStairs(self, n: int) -> int:
        prev2 = 1  # ways to reach step 0
        prev1 = 1  # ways to reach step 1

        for _ in range(2, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return prev1