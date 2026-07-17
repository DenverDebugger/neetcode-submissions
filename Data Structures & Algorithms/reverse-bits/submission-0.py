class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = [] 

        for i in range(32):
                res.append(n & 1)
                n >>= 1
        print(res)
        
        # convert to base 10
        s = "".join(str(bit) for bit in res)

        return(int(s, 2))