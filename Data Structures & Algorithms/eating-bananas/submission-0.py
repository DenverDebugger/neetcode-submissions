class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # find minimum number of bananas needed
        # to eat all bananas in 'h' hours
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            total = 0

            for pile in piles:
                total += math.ceil(pile / mid)

            if total <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left
