def countSubstrings(s: str) -> int:
        n, ans = len(s), 0

        def countPalindrome(left: int, right:int) -> int:
            count = 0

            while left >= 0 and right < n and s[left] == s[right]:
                left -=1
                right += 1
                count += 1
            
            return count

        for i in range(n):
            even = countPalindrome(i, i + 1)
            odd = countPalindrome(i,i)
            ans += odd + even
        
        return ans