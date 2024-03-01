def reorderLogFiles(logs: l[str]) -> List[str]:
    letterLogs = []

    digitLogs = []

    for i in logs:
        if i.split(" ")[1].isdigit():
            digitLogs.append(i)
        else:
            heapq.heappush(letterLogs, (' '.join(i.split(" ")[1:]), i))
    
    result = [heapq.heappop(letterLogs)[1] for _ in range(len(letterLogs))]
    result.extend(digitLogs)
    return result