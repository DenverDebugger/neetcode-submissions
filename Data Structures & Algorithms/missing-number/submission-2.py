class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0

        # xor the expected nums
        for i in range(len(nums) + 1):
            res ^= i

        # xor the actual nums
        for j in range(len(nums)):
            res^= nums[j]

        return res
