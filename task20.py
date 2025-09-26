
permissions = {"read": True, "write": False, "delete": True}

true_keys = []

for key, boolen in permissions.items():
    if boolen == True:
        true_keys.append(key)

print(true_keys)