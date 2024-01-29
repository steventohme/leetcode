# Naive Solution O(n^2) time complexity, O(1) space complexity
def twoSumNaive(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]

# Optimal Solution O(n) time complexity, O(n) space complexity
def twoSum(nums: list[int], target: int) -> list[int]:
    compliments = {}

    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in compliments:
            return [compliments[compliment], i]
        else:
            compliments[nums[i]] = i
