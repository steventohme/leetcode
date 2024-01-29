# Naive Solution

def twoSumNaive(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]

def twoSum(nums: list[int], target: int) -> list[int]:
    pass

if __name__ == "__main__":
    print(twoSumNaive([2, 7, 11, 15], 9))