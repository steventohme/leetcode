def lengthOfLongestSubstring(self, s: str) -> int: 
    longest = 0
    l = 0
    chars = set()

    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[r])
            l += r
            

    return longest