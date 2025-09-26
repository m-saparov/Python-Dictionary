def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}

    for student in students:
        name = student["name"]
        group = student["group"]

        if group not in groups:
            groups[group] = []

        groups[group].append(name)

    return groups


def main():
    students = [
        {"name": "Ali", "group": "A"},
        {"name": "Vali", "group": "B"},
        {"name": "Soli", "group": "A"},
        {"name": "Karim", "group": "B"},
    ]

    result = group_students(students)
    print(result)


main()
