def reverseVowels(s: str) -> str:
    def isVowel(char:str) ->bool:
        if char in "aeiouAEIOU":
            ret