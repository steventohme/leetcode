def findErrorNums(nums: list[int]) -> list[int]:
    n = len(nums)
    expectedSum = (n * (n + 1)) // 2
    
    arraySum = sum(nums)
    uniqueSum = sum(set(nums))

    missing = expectedSum - uniqueSum
    duplicate = arraySum - uniqueSum


    return [missing, duplicate]
        
    
print(findErrorNums([1,2,2,4]))