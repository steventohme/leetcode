def sequentialDigits(self, low: int, high: int) -> list[int]:
    maximum = "123456789"
    res = []

    start = 0
    size = 1

    while size < 9:
        
        if start == 9:
            size += 1
            start = 0