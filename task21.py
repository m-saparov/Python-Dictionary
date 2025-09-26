def count_names(names: list[str]) -> dict[str, int]:
    counts = {}
    for name in names:
        counts[name] = counts.get(name, 0) + 1
        
    return counts


def main():
    names = ["Ali", "Vali", "Ali", "Sami", "Vali", "Ali"]
    result = count_names(names)
    print(result) 

main()