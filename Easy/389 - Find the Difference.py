from collections import defaultdict
def findTheDifference(s: str, t: str) -> str:
    chars_s = defaultdict(int)
    for i in s:
        chars_s[i] += 1
    
    chars_t = defaultdict(int)
    for i in t:
        chars_t[i] += 1
    
    
