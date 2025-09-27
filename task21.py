def count_names(names: list[str]) -> dict[str, int]:
    counts = {}
    for name in names:
        counts[name] = counts.get(name, 0) + 1
        
    return counts

def count_names2(names: list[str]) -> dict[str, int]:
    unique_names = set()
    for name in names:
        unique_names.add(name)
    result = {}
    for name in unique_names:
        result[name] = 0
    for name in result.keys():
        result[name] = names.count(name)

    return result

def main():
    names = ["Ali", "Vali", "Ali", "Sami", "Vali", "Ali"]
    result = count_names(names)
    print(result) 

main()