person = {"name": "Ali", "age": 25, "city": "Tashkent"}

del person["city"] # city bo'lmasa error
person.pop("city", None) # errorsiz

print(person)