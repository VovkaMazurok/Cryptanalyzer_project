def read_and_split_file(file_path):
    try:
        with open(file_path, encoding="utf-8") as file:
            # Читаємо всі рядки з файлу та видаляємо зайві символи нового рядка
            words = file.read().splitlines()
            # Об'єднуємо всі слова через пробіл
            result = " ".join(words)
        return result
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        return ""
