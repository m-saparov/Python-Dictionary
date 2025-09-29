def count_letters(text: str) -> dict[str, int]:
    res = dict()
    for ch in text:
        # agar bo'sh joyni hisoblamaslik kerak bo'lsa:
        # if ch == ' ':
        #     continue
        if ch not in res:
            res[ch] = 0
        res[ch] += 1
    
    return res

print(count_letters("ssll oo aa sl a"))

