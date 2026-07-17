class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0
        # process all 32 bits
        for i in range(32):
            # get last bit
            bit = n & 1

            # shift result left to make room
            res = res << 1

            # insert extracted bit
            res = res | bit
            
            # move to next bit in n
            n = n >> 1
        return res