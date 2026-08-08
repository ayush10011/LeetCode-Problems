class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        a = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        num = 1

        while top <= bottom:
            for j in range(left, right + 1):
                a[top][j] = num
                num += 1
            top += 1

            for i in range(top, bottom + 1):
                a[i][right] = num
                num += 1
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    a[bottom][j] = num
                    num += 1
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    a[i][left] = num
                    num += 1
                left += 1

        return a