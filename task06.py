car = {"brand": "Chevrolet", "model": "Cobalt", "color": "white"}

keyword = input("Key: ").lower()

result = "Bunday key mavjud emas!"

for key in car:
    if key == keyword:
        result = car[key]

print(result)
