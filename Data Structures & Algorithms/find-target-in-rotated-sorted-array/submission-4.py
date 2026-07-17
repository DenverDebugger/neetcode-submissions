class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # Binary Search
        while l <= r:
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid

            # [4, 5, 6, 7, 0, 1, 2] , t = 1
            # [7, 0, 1, 2, 4, 5, 6], t =1

            # left sorted portion
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1

            # right sorted portion
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1