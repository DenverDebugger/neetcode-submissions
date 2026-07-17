class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        
        def dfs(start, remaining):
            # we found a valid combination
            if remaining == 0:
                ans.append(path.copy())
                return

            # we chose a number too big
            if remaining < 0:
                return

            # horizontal choices: i.e. exploring
            for i in range(start, len(nums)):
                choice = nums[i]

                # choose
                path.append(choice)

                # Explore
                dfs(i, remaining - choice)

                # unchoose
                path.pop()

        dfs(0, target)
        return ans

            