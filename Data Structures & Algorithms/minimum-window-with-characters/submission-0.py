class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        # these are to count the frequencies of the chars in t and
        # your sliding window
        count_t = {}
        window = {}

        # get a frequency count for string t
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)

        # these are to keep track of how many frequencies are satisfied
        have = 0
        need = len(count_t)

        # these are to keep track of the start and end of valid substrings
        # and to know when you have found a shorter one, so you can update
        # start_end if needed
        start_end = [0, 0]
        min_res = float("inf") # to keep track of window size

        # two pointer iteration, right grows first
        l = 0
        for r in range(len(s)):
            # add char to your window
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            # if char is in our t hashmap, and frequencies are the same
            # then we can increment have because we have satisfied one requirement
            # NOTE: this will not increment if frequencies are different
            if char in count_t and window[char] == count_t[char]:
                have += 1

            # Shrink from left if we have a valid window
            while have == need:
                # check window size, and store if needed
                if r - l + 1 < min_res:
                    start_end = [l, r]
                    min_res = r - l + 1

                # decrement frequency of char at left pointer in current window
                window[s[l]] -= 1 
                # check if that char was a requirement and decrement if needed
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                # move left pointer to the right
                l += 1
        return s[start_end[0]: start_end[1] + 1] if min_res != float("inf") else ""


































