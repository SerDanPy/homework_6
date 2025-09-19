"""4. Генератор для обробки великих файлів
Реалізуйте генератор, який читає великий текстовий файл рядок за рядком (наприклад, лог-файл) і повертає лише ті рядки, що містять певне ключове слово. Використайте цей генератор для фільтрації файлу та запису відповідних рядків у новий файл."""


def filter_file(filename, keyword):
    """Generator to yield lines containing a specific keyword"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if keyword in line:
                    yield line.strip()
    except FileNotFoundError:
        print(f"Помилка: Файл з іменем '{filename}' не знайдено")


if __name__ == "__main__":
    #Create log file
    with open("test.log", "w", encoding="utf-8") as file:
        file.write("INFO: TEST\nERROR: ERROR404\nINFO: TEST\nERROR: ERROR500\nLINE: TEST\nERROR: ERROR100")

    #Filter and save lines with keyword
    with open("errors.log", "w", encoding="utf-8") as output_file:
        for line in filter_file("test.log", "ERROR"):
            print(line)
            output_file.write(line + "\n")

