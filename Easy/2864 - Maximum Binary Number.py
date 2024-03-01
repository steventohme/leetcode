def maximumOddBinaryNumber(s: str) -> str:
    i_count = s.count("1")

    return "1" * (i_count - 1) + "0" * (len(s) - i_count) + "1"