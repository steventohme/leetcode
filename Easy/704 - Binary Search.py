def search(A: list[int], X: int) -> int:
    l,r = 0, len(A) - 1

    while l <= r:
        mid = (l +r) // 2
        if A[mid] == X:
            return mid
        elif A[mid] > X:
            r = mid - 1
        else:
            l = mid + 1
    
    return -1