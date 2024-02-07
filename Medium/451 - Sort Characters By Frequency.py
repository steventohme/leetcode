import collections

# O(nlogn) time complexity and O9n
 def frequencySort(s: str) -> str:
    count = collections.defaultdict(int)
    for char in s:
        count[char] += 1
    
    res = []
    for k,v in sorted(count.items(), key = lambda x: -x[1]):
        res += [k] * v
    
    return ''.join(res)