class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        largest = 0

        for i in range(len(heights)):
            while len(stack) != 0 and heights[i] < stack[-1][1]:
                # pop element
                curr_index, curr_height = stack.pop()

                # calculate area
                right = i
                left = stack[-1][0] if stack else -1

                curr_area = curr_height * (right - left -1)
                largest = max(largest, curr_area)
            stack.append((i, heights[i]))
            
        return largest