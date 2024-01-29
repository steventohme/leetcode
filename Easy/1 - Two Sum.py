# Naive Solution O(n^2) 
def twoSumNaive(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]

# Optimal Solution
def twoSum(nums: list[int], target: int) -> list[int]:
    compliments = {}

    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in compliments:
            return [compliments[compliment], i]
        else:
            compliments[nums[i]] = i
