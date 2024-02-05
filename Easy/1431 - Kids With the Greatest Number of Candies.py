def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    res = [True] * len(candies)
    greatest = max(candies)

    for i in range(len(candies)):
        res[i] 