class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0

        for i in range(len(heights)):
            left = i
            right = i

            while left - 1 >= 0 and heights[left - 1] >= heights[i]:
                left -= 1

            while right + 1 < len(heights) and heights[right + 1] >= heights[i]:
                right += 1

            width = right - left + 1 # 5 - 2 =3 but left bound should be included, so add back one = 4 X max height = 2.... 4x2 = 8
            area = heights[i] * width
            largest = max(largest, area)
        
        return largest