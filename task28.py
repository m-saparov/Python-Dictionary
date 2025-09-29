
def group_by_length(words: list[str]) -> dict[int, list[str]]:
    result: dict[int, list[str]] = {}

    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    
    return result

words = [
    "apple",
    "banana",
    "cherry",
    "orange",
    "grape",
    "mango",
    "peach",
    "melon",
    "plum",
    "kiwi"
]

print(group_by_length(words))
