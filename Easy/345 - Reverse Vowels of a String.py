def reverseVowels(s: str) -> str:
    def isVowel(char:str) ->bool:
        if char in "aeiouAEIOU":
            return True
        
        return False
    
    string_list = list(s)

    l,r = 0, len(string_list) - 1

    while l < r:
        if isVowel(string_list[l]) and isVowel(string_list[r]):
            string_list[l], string_list[r] = string_list[r], string_list[l]
            l += 1
            r -= 1
        
        elif not isVowel(string_list[l]):
            l += 1
        
        elif not isVowel(string_list[r]):
            r -= 1
    
    return ''