def groupAnagrams(strs: list[str]) -> list[list[str]]:
    word_list = {}
    for i in range(strs):
        key = s