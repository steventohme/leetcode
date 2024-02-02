def sequentialDigits(self, low: int, high: int) -> list[int]:
    maximum = "123456789"
    res = []

    start = 0
    size = 1

    while size < 9:
        currentNum = int(maximum[start: start + size])
        if currentNum > low and currentNum < high:
            res.append(currentNum)
        
        if start + size == len(maxim):
            size += 1
            start = 0
