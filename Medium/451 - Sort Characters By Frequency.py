import collections

def frequencySort(s: str) -> str:
    count = collections.defaultdict(int)
    for char in s:
        count[char] += 1
    
    