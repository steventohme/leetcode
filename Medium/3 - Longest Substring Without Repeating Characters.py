# Naive Solution
def lengthOfLongestSubstringNaive(self, s: str) -> int:
    longest = 0
    for i in range(len(s)):
        chars = set()
        for j in range(i, len(s)):
            if s[j] in chars:
                break
            else:
                chars.add(s[j])
        longest = max(longest, len(chars))
    return longest

# Optimal Solution
def lengthOfLongestSubstring(self, s: str) -> int: 
    longest = 0
    l = 0
    chars = set()
    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[l])
            l += 1
        
        chars.add(s[r])
        longest = max(longest, r - l + 1)

    return longest