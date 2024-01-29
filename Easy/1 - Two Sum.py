# Naive Solution

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

if __name__ == "__main__":
    print(twoSumNaive([2, 7, 11, 15], 9))
    print(twoSumNaive([3, 2, 4], 6))
    print(twoSumNaive([3, 3], 6))

    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([3, 2, 4], 6))
    print(twoSum([3, 3], 6))