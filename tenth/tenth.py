"""10. Архівування та зберігання великих даних
Реалізуйте менеджер контексту для архівування файлів (за допомогою модуля zipfile).
Менеджер автоматично створює архів, додає файли, а після виходу з блоку with – завершує архівування та закриває архів."""

import zipfile
import os


class ArchiveManager:
    """Create class ArchiveManager with functions"""

    def __init__(self, archive_name, files):
        #Initialize
        self.archive_name = archive_name
        self.files = files
        self.zip_file = None

    def __enter__(self):
        #Enter file
        self.zip_file = zipfile.ZipFile(self.archive_name, 'w', zipfile.ZIP_DEFLATED)
        for file in self.files:
            if os.path.exists(file):
                self.zip_file.write(file)
        return self.zip_file

    def __exit__(self, exc_type, exc_value, traceback):
        #Exit file
        self.zip_file.close()


if __name__ == "__main__":
    #Create test files
    with open("file1.txt", "w", encoding="utf-8") as file:
        file.write("А це дані")
    with open("file2.txt", "w", encoding="utf-8") as file:
        file.write("Ще раз якісь дані")

    # Create archive
    with ArchiveManager("archive.zip", ["file1.txt", "file2.txt"]):
        pass
    print("Архів створено archive.zip")


""" name_archive = input("Введіть ім'я архіву\n--->")
    with ArchiveManager(name_archive, ["file1.txt", "file2.txt"]):
        pass

    print(f"Архів створено з іменем: {name_archive}.zip ")"""
