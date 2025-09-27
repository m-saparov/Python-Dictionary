def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    grouped = {}

    for person in people:
        grouped.setdefault(person["age"], []).append(person["name"])

    return grouped


people = [
    {"name": "Ali", "age": 20},
    {"name": "Vali", "age": 22},
    {"name": "Sami", "age": 19},
    {"name": "Hasan", "age": 25},
    {"name": "Husan", "age": 24},
    {"name": "Olim", "age": 23},
    {"name": "Dilshod", "age": 21},
    {"name": "Javohir", "age": 26},
    {"name": "Shahzod", "age": 27},
    {"name": "Bekzod", "age": 28},
    {"name": "Umid", "age": 29},
    {"name": "Rustam", "age": 30},
    {"name": "Kamol", "age": 18},
    {"name": "Farrux", "age": 20},
    {"name": "Aziz", "age": 22},
]

print(group_by_age(people))
