class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # one spot for each letter in the alphabet
        count = [0] * 26

        # these are all lowercase so we should be able to "normalize"
        # them to take up a spot between 0-to-25, that way our array works
            # this is necessary because 'a' is ascaii 97
            # so ord('a') - ord('a') = 0
            # ord('b') - ord('a') = 1,....ord('z') - ord('a') = 25

            # scan through both strings
        for i in range(len(s)):
            # increment the count of the letter for every letter in s
            count[ord(s[i]) - ord('a')] += 1 
            # decrement the count of the letter for every letter in t
            count[ord(t[i]) - ord('a')] -= 1

        # see if they all canceled out
        for val in count:
            if val != 0:
                return False
        # all vals were zero so the words must contain the same strings
        return True