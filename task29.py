def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    active_list = []
    for user in users.values():
        if user["active"] == True:
            active_list.append(user["name"])
    return active_list


users = {
    "user1": {"name": "Ali", "active": True},
    "user2": {"name": "Vali", "active": False},
    "user3": {"name": "Hasan", "active": True},
    "user4": {"name": "Husan", "active": False},
}

print(get_active_users(users))
