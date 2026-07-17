class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # set up dict with freq of chars in s1
        # init L, R, res, s2_dict
        # iterate through s2, 
            # keep a window of size len(s1)
            # for each new char, increment s2_dict
            # if window size == len(s1) and not answer
            # decrement from left and keep going until find answer
            # or array ends. 

            l = r = 0
            s1_map = {}
            s1_len = len(s1)
            s2_len = len(s2)

            for char in s1:
                s1_map[char] = 1 + s1_map.get(char, 0)

            window = {}
            for r in range(len(s2)):
                # add new item
                window[s2[r]] = 1 + window.get(s2[r], 0
                )
                # if window to big, shrink
                if r - l + 1 > s1_len:
                    window[s2[l]] -= 1

                    if window[s2[l]] == 0:
                        del window[s2[l]]

                    l += 1

                # if window sz, and freq are correct return True
                if r - l + 1 == s1_len and window == s1_map:
                    return True
            
            return False