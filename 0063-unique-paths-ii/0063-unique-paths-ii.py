class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        dp = [1] + [0] * (len(obstacleGrid[0]) - 1)

        for row in obstacleGrid:
            for j, cell in enumerate(row):
                if cell:
                    dp[j] = 0
                elif j:
                    dp[j] += dp[j - 1]

        return dp[-1]