status = ""

match status:
    case "active":
        print("Пользователь активен.")
    case "inactive":
        print("Пользователь неактивен.")
    case _:
        print("Неизвестный статус.")