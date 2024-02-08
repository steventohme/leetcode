
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n == -1:
        return 1/x
    # x^10 = x^5 * x^5 * x^0
    return myPow(x, n//2) * myPow(x, n//2) * myPow(x, n%2)