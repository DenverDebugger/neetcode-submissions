class Solution:
    def climbStairs(self, n: int) -> int:
        # key: take step, don't take step
        # what are the base cases?
            # step = n: no more steps
        cache = {}

        def take(step):
            if step == n:
                return 1
            elif step > n:
                return 0
            else:
                if step in cache:
                    return cache[step]
                takeOne = take(step + 1)
                takeTwo = take(step + 2)
                cache[step] = takeOne + takeTwo

            return cache[step]
        
        return take(0)