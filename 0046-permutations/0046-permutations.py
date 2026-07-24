from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(first):
            if first == len(nums):
                ans.append(nums[:])
                return

            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                dfs(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        dfs(0)
        return ans