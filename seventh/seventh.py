"""7. Парсинг великих лог-файлів для аналітики
Уявіть, що у вас є великий лог-файл від веб-сервера. Створіть генератор, який зчитує файл порціями (по рядку) і повертає тільки рядки з помилками (код статусу 4XX або 5XX). Запишіть ці помилки в окремий файл для подальшого аналізу."""


def parse_errors(filename):
    """Generator to yield log lines with 4XX or 5XX status codes"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                if any(code in line for code in (' 4', ' 5')):
                    yield line.strip()
    except FileNotFoundError:
        print(f"Помилка: Файл з іменем '{filename}' не знайдено")


if __name__ == "__main__":
    #Create log file
    with open("logs.log", "w", encoding="utf-8") as file:
        file.write("200 OK: GET /index.html\n404 Not Found: GET /page\n500 Error: POST /api\n404 Error")

    #Save errors
    with open("errors.log", "w", encoding="utf-8") as output_file:
        for line in parse_errors("logs.log"):
            print(line)

            output_file.write(line + "\n")
