def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    stack = []
    res = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            res[j] = i - j
        
        stack.append(i)