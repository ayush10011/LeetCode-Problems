class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # stores indices
        max_area = 0

        # Add a 0 to force processing of all remaining bars
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                # After popping, stack[-1] is the first smaller bar on the left
                left = stack[-1] if stack else -1
                width = i - left - 1

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area