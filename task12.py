
inventory = {"apple": 10, "banana": 5}

product = input("Mahsulot: ")

inventory.setdefault(product, 0)

print(inventory)
