class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = nums[:k]
        res.append(max(window))
    
        for r in range(k, len(nums)):
            window.append(nums[r])

            if len(window) > k:
                del window[0]
            res.append(max(window))

        return res