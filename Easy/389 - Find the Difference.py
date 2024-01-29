from collections import defaultdict
# O(n) time and O(1) space complexity
def findTheDifference(s: str, t: str) -> str:
    chars_s = defaultdict(int)
    for i in s:
        chars_s[i] += 1
    
    chars_t = defaultdict(int)
    for j in t:
        chars_t[j] += 1
    
    for k in chars_t:
        if chars_s[k] != chars_t[k]:
            return k
    
