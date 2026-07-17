class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while(n):
            tmp = n & 1
            if tmp:
                count += 1
            n = n>>1
        return count    