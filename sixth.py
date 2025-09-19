"""6. Ітерація через файли в каталозі
Напишіть ітератор, який буде повертати всі файли в заданому каталозі по черзі. Для кожного файлу виведіть його назву та розмір."""

import os


class DirectoryIterator:
    """Iterator to yield files and their sizes in a directory"""

    def __init__(self, directory):
        #Initialize with directory path
        self.directory = directory
        self.files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        self.index = 0

    def __iter__(self):
        #Return the iterator object
        return self

    def __next__(self):
        #Return the next file and its size
        if self.index >= len(self.files):
            raise StopIteration
        filename = self.files[self.index]
        filepath = os.path.join(self.directory, filename)
        size = os.path.getsize(filepath)
        self.index += 1
        return {'filename': filename, 'size': size}


if __name__ == "__main__":
    for file_info in DirectoryIterator("C:/Program Files (x86)/Adobe/Acrobat Reader DC/Reader/acrocef_1"):

        print(f"Файл: {file_info['filename']}, Розмір: {file_info['size']} байтів")
