class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        i = 0
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                last_index = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                area = heights[last_index] * width
                max_area = max(max_area, area)
                
        while len(stack) > 0:
            last_index = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            area = heights[last_index] * width
            max_area = max(max_area, area)

        return max_area