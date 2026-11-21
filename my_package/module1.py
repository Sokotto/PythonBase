def find_phone(filename, surname, initials):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split()

                if len(parts) < 3:
                    continue

                if (parts[0].lower() == surname.lower() and
                        parts[1].lower() == initials.lower()):
                    return parts[2]
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return None
    return None
def main():
    filename = "T.txt"
    surname = input("Введите фамилию: ").strip()
    initials = input("Введите инициалы (например, И.И.): ").strip()

    phone = find_phone(filename, surname, initials)
    if phone:
        print(f"Телефон сотрудника {surname} {initials}: {phone}")
    else:
        print(f"Сотрудник {surname} {initials} не найден.")
if __name__ == "__main__":
    main()
