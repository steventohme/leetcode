def findErrorNums(self, nums: list[int]) -> list[int]:
    n = len(nums)
    expectedSum = (n * (n + 1)) / 2
    seen = set()
    arraySum = sum(nums)

    for i in nums:
        seen.add()
        