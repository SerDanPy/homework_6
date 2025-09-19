"""9. Автоматичне резервне копіювання

Напишіть менеджер контексту, який буде створювати резервну копію важливого файлу перед його обробкою. Якщо обробка пройде успішно, оригінальний файл замінюється новим. У разі помилки резервна копія автоматично відновлюється."""

import shutil
import os


class BackupManager:
    """Create class BackupManager with functions of opening, closing a file and creating a backup copy"""

    
    def __init__(self, filename):
        #Initialize
        self.filename = filename
        self.backup_filename = filename + ".bak"

    def __enter__(self):
        if os.path.exists(self.filename):
            shutil.copy(self.filename, self.backup_filename)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None and os.path.exists(self.backup_filename):
            shutil.move(self.backup_filename, self.filename)
            print(f"Помилка! Резервне копіювання файлу з іменем {self.filename}")
        elif os.path.exists(self.backup_filename):
            os.remove(self.backup_filename)


if __name__ == "__main__":
    #Create test file
    with open("data.txt", "w", encoding="utf-8") as file:
        file.write("Початкові дані\nДані початкові\nЯкісь дані\nЩе раз якісь дані")

    #Testing success
    with BackupManager("data.txt"):
        with open("data.txt", "w", encoding="utf-8") as file:
            file.write("А це нові дані\nЩе раз якісь нові дані\nІ можна ще раз якісь дані")
    print("Файл успішно оновлено")

    #Testing error
    print("\nТестування помилки")
    try:
        with BackupManager("data.txt"):
            with open("data.txt", "w", encoding="utf-8") as file:
                file.write("Нові дані з помилками")
            raise ValueError("Імітація помилок")
    except ValueError:
        print("")

    #Check file content
    with open("data.txt", "r", encoding="utf-8") as file:

        print(f"Остаточний варіант: {file.read()}")
