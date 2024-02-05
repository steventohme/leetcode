def reverseVowels(s: str) -> str:
    def isVowel(char:str) ->bool:
        if char in "aeiouAEIOU":
            return True
        
        return False
    
    string_list = list(s)

    l,r = 0, len(string_list)