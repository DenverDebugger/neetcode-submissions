class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = {}

        for letter in s:
            if s_freq.get(letter, 0):
                s_freq[letter] = s_freq[letter] + 1
            else:
                s_freq[letter] = 1

        for letter in t:
            if s_freq.get(letter, 0):
                s_freq[letter] -= 1
            else:
                return False

        return True