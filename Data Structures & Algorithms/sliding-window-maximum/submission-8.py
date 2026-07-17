class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []

        for r in range(len(nums)):
            heapq.heappush(heap, (-nums[r], r))

            if r + 1 - k >= 0:
                while heap[0][1] < r + 1 - k:
                    heapq.heappop(heap)

                res.append(-heap[0][0])
        
        return res