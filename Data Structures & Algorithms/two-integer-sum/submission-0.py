class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        # you have to store the value as the key so that you can use
        # the O(1) lookup to check if diff is in the keys
        for i, v in enumerate(nums):
            indices[v] = i
        
        # check if diff (target minus value(which is a dict key)) is in the hashmap
        # check if the index of target minus value is not equal to your current index
        # if both check pass return current index, and index of diff
        for i, v in enumerate(nums):
            diff = target - v
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []