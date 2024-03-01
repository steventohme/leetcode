def isValid(s: str) -> bool:
    stack = []

    parentheses = {"{": "}", "(": ")", "[": "]"}

    for bracket in s:
        if bracket in parentheses:
            stack.append(bracket)
        elif stack:
            open_bracket = stack.pop()
            if parentheses[open_bracket] != bracket:
                return False
        else:
            return False
    
    return len(stack) == 0