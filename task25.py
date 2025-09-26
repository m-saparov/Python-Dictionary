def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    grouped = {}

    for person in people:
        age = person["age"]
        name = person["name"]

        if age not in grouped:
            grouped[age] = []
        grouped[age].append(name)

    return grouped

people = [
    {"name": "Ali", "age": 20},
    {"name": "Vali", "age": 22},
    {"name": "Hasan", "age": 20},
    {"name": "Husan", "age": 23},
    {"name": "Dilshod", "age": 22},
]

print(group_by_age(people))
