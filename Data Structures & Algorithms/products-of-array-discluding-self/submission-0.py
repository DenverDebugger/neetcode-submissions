class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        res = []

        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
            # i = 1: pre[1] = 1 * 1
            # i = 2: pre[2] = 1 * 2
            # i = 3: pre[3] = 2 * 4
            # pre = [1, 1, 2, 8]

        for i in range(len(nums)-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
            # i = 2: post[2] = 1 * 6
            # i = 1: post[1] = 6 * 4
            # i = 0: post[0] = 24 * 2
            # post = [48, 24, 6, 1]

        for i in range(len(nums)):
            res.append(post[i]*pre[i])
            # i = 0: res = 48
            # i = 1: res = 48, 24 
            # i = 2: res = 48, 24, 12
            # i = 3: res = 48, 24, 12, 8
        
        return res

        # this code could be improved a lot:
        # 1. keep a running calculation instead of storing in arrays
        # 2. stop calculating len(nums)
        

        
