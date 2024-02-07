import collections

# O(nlogk) time complexity and O(n) space complexity
def frequencySort(s: str) -> str:
    count = collections.defaultdict(int)

    
    res = []
    for k,v in sorted(count.items(), key = lambda x: -x[1]):
        res += [k] * v
    
    return ''.join(res)