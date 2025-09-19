"""3. Збір статистики про зображення
У вас є каталог з великою кількістю зображень. Напишіть ітератор, який по черзі відкриває кожне зображення (наприклад, за допомогою модуля PIL), витягує з нього метадані (розмір, формат тощо) і зберігає ці дані у файл CSV."""

import os
import csv
from PIL import Image


class ImageStatsIterator:
    """Iterator to collect image metadata from a directory"""

    def __init__(self, directory, csv_filename):
        """Initialize with directory and CSV output file"""
        self.directory = directory
        self.csv_filename = csv_filename
        self.files = [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg'))]
        self.index = 0
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Filename', 'Width', 'Height', 'Format'])

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.files):
            raise StopIteration
        filename = self.files[self.index]
        filepath = os.path.join(self.directory, filename)
        try:
            with Image.open(filepath) as img:
                width, height = img.size
                format = img.format
                with open(self.csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([filename, width, height, format])
                self.index += 1
                return {'filename': filename, 'width': width, 'height': height, 'format': format}
        except Exception as e:
            self.index += 1
            return {'filename': filename, 'error': str(e)}


if __name__ == "__main__":
    iterator = ImageStatsIterator("images", "image_stats.csv")
    for stats in iterator:
        print(stats)