# O(n) time complexity and O(1) space complexity
def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if n == 0:
        return True

    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) -1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            n -=1
            if n == 0:
                return True
    
    return False