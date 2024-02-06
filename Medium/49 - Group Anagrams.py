def groupAnagrams(strs: list[str]) -> list[list[str]]:
    word_list = {}
    for i in range(strs):
        key = str(sorted(i))

        if key in word_list:
            word_list[key]