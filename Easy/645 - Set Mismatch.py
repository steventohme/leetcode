def findErrorNums(self, nums: list[int]) -> list[int]:
    n = len(nums)
    expectedSum = (n * (n + 1)) / 2
    
    arraySum = sum(nums)
    uniqueArray = set(nums)
        
    
