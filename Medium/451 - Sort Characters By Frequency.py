import collections

# O(nlogk) time complexity and O(n) space complexity
def frequencySort(s: str) -> str:
    count = collections.Counter(s)

    
    res = []
    for k,v in count.most_common():
        res += [k] * v
    
    return ''.join(res)