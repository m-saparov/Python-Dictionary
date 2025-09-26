def most_common_char(text: str) -> str:
    char_count: dict[str, int] = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    most_common = max(char_count, key=char_count.get)
    return most_common


def main():
    text = "hello world"
    result = most_common_char(text)
    print(f"Eng ko'p uchragan belgi: {result}")


main()
