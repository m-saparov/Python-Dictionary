def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    res = {}
    for key, value in d.items():
        if value != 0:
            res[key] = value
    return res

data = {
    "a": 5,
    "b": 0,
    "c": 7,
    "d": 0,
    "e": 3
}

print(filter_non_zero(data))
