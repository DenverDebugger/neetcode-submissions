class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x, y = nums1, nums2

        if len(x) > len(y):
            x, y = y, x

        total = len(x) + len(y)
        half = total // 2 # how many elements should be on the left side of the array
        
        l, r = 0, len(x)
        while True:
            # keep in mind that i, and j are partitions, not indices we are searching over
            i = (l + r) // 2 # how many elements from x on the left
            j = half - i # how many elements from y go on the left

            # this handles edge cases where you select either none or all of the elements
            # from one of the given arrays
            x_left = x[i-1] if i > 0 else float("-inf")
            x_right = x[i] if i < len(x) else float("inf")
            y_left = y[j-1] if j > 0 else float("-inf")
            y_right = y[j] if j < len(y) else float("inf")

            # TODO: implement check if at right partition
            if x_left <= y_right and y_left <= x_right: # correct partition found
                # TODO: return correct value for median
                    # why these checks? see below
                    # [1,3], [2,4]
                    # [1 | 3]
                    # [2 | 4]
                    # median is (2+3) / 2 but to get at that we use our variables from above
                    # and some functions since all we know at this point is that correct partition is found
                    # BUT there is no gaurantee on whether x_left being < y_left, or x_right being > y_right
                    # so here: max(max(1,2) + min(3,4)) / 2 = (2+3) / 2 = 2.5
                if total % 2 == 0:
                    return (max(x_left, y_left) + min(x_right, y_right)) / 2
                else:
                    # ODD case: [1,2], [3]
                    # [1 | 2] 
                    # [| 3]
                    # min(2, 3) = 2 which is the median!
                    return min(x_right, y_right)
            
            # TODO: update i, and j if partition not found
            if x_left > y_right:
                r = i - 1
            else:
                l = i + 1