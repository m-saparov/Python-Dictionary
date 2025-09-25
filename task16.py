settings = {
    "theme": "dark",
    "volume": 80,
    "language": "uz"
}

keywoord = input("Kalit: ")

removed = settings.pop(keywoord, None)

if removed is None:
    print("Bunday kalit yoq")
else:
    print(f'"{keywoord}" kaliti ochirildi')

print(settings)
