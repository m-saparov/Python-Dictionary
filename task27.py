def is_valid(number: str) -> bool:
    return number.isdigit() and (len(number) == 9 or len(number) == 11)

def add_contact(phonebook: dict[str, str]) -> None:
    name = input("Enter Name: ")

    while True:
        number = input("Phone Number: ")
        if is_valid(number):
            phonebook[name] = number
            break
        else:
            print("Phone Number xato!")

def show_contacts(phonebook: dict[str, str]) -> None:
    if not phonebook:
        print("Hozircha Bo'sh")
        return
    
    for contact in phonebook:
        print(f"{contact}: {phonebook[contact]}")

def search_contact(phonebook: dict[str, str]) -> None:
    results = {}
    search = input("Search: ")

    for contact in phonebook:
        if search in contact or search in phonebook[contact]:
            results[contact] = phonebook[contact]
    
    if results:
        print("Natijalar: ")
        show_contacts(results)
    else:
        print("Hech narsa topilmadi.")

def phonebook_menu(phonebook: dict[str, str]) -> None:
    while True:
        print("-----MENU-----")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Search Contact")
        print("0. Exit")

        choice = input("Choice: ")
        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            show_contacts(phonebook)
        elif choice == "3":
            search_contact(phonebook)
        elif choice == "0":
            print("You left!")
            break
        else:
            print("Faqat (1/2/3/0) tanlay olasiz!")


phonebook = {
    "Ali": "901112233",
    "Vali": "902223344",
    "Sami": "903334455",
    "Hasan": "904445566",
    "Husan": "905556677",
    "Madina": "906667788",
    "Dilshod": "907778899",
    "Gulbahor": "908889900",
    "Jasur": "909990011",
    "Saida": "901234567"
}

phonebook_menu(phonebook)
