class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            curr_area = width * height
            max_area = max(max_area, curr_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area