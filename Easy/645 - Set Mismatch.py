def findErrorNums(self, nums: list[int]) -> list[int]:
    n = len(nums)
    expectedSum = (n * (n + 1)) // 2
    
    arraySum = sum(nums)
    uniqueSum = sum(set(nums))

    missing = expectedSum - uniqueSum
    duplicate = expectedSum - arraySum


    return [missing, duplicate]
        
    
