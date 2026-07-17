class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for  num in nums:
            count[num] = 1 + count.get(num, 0)

        heap = []
         # heapq compares the first element in a tuple (x, y)
        # that's why push them on in this order
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

