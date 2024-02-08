def topKFrequent(nums: list[int], k: int) -> list[int]:
    frequency_dict = {}
    for i in nums:
        if i in frequency_dict:
            frequency_dict[i] += 1
        else:
            frequency_dict[i] = 1
    
    sortedList = sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)
    res = sortedList[:k]
    return_list = []
    for i in res:
        return_list.append(i[0])
    return return_list