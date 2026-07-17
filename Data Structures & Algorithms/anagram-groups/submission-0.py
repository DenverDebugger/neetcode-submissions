class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    # defualtdict prevents errors from occuring when checking for keys that may not be in dict
       anagrams = defaultdict(list) # list is the type of thing anagrams stores

    # iterate through, sort the string, store the sorted string as a key and append the original string as the value
       for s in strs:
        temp_s = ''.join(sorted(s)) # sorted return a iterable list of chars so it must be joined back to be a string.
        anagrams[temp_s].append(s) # since defaultdict stores list's, we can directly append to it

    # return the values of the dict as your answer
       return anagrams.values()