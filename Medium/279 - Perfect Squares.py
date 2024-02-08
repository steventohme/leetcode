def numSquares(n: int) -> int:
    def solve(n):
        if n == 0:
            return 0

        if n < 0:
            return float("inf")
        
        if memo[n] != -1:
            return memo[n]
        
        mini = n
        i = 1
        while i * i <=n:
            mini = min(mini, solve(n - (i*i)))
            i += 1
        
        memo[n] = mini + 1
        return memo[n]
    
    memo = [-1] * (n + 1)
    return solve(n)