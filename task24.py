def most_common_char(text: str) -> str:
    mx = text[0]
    for ch in text:
        if text.count(ch) > text.count(mx):
            mx = ch
    return mx


def main():
    text = "hello world"
    result = most_common_char(text)
    print(f"Eng ko'p uchragan belgi: {result}")


main()
