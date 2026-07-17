class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        encoded = []

        for s in strs:
            length = str(len(s))
            encoded.append(length + "#" + s)
        return "".join(encoded)
        # // 3#cat4#dog44#code4#lint

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        n = len(s)

        i = 0
        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) # this extracts the number
            # now we need to extract the string which resides in
            # str from index j+1 to j+1+length
            start = j + 1
            end = start + length
            res.append(s[start:end]) # in python 'end' is not kept, everything up until it is.
            i = end
        return res

             