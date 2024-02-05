import collections
# O(n) time complexity and O(1) space complexi
def firstUniqChar(s: str) -> int:
    counts = collections.Counter(s)

    for i in range(len(s)):

        if counts[s[i]] == 1:
            return i
        
    return -1