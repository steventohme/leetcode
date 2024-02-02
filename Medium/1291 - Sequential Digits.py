def sequentialDigits(self, low: int, high: int) -> list[int]:
    maximum = "123456789"
    res = []

    for l in range(9):
        for r in range(9):
            if maximum[l:r] > low and maximum[l:r] < high:
                res.append(int())