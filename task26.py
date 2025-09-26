def merge_dicts(a: dict, b: dict) -> dict:
    merged = a.copy() 
    merged.update(b) 
    return merged

x = {"name": "Ali", "age": 20}
y = {"age": 25, "city": "Tashkent"}

print(merge_dicts(x, y))
