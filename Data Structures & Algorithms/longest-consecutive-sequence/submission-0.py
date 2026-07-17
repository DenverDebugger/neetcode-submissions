class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        longest = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in hs:
                curr_length = 1
                while nums[i] + curr_length in hs:
                    curr_length += 1
                longest = max(longest, curr_length)
        return longest