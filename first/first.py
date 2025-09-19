"""1. Створення власного ітератора для зворотного читання файлу
Напишіть власний ітератор, який буде зчитувати файл у зворотному порядку — рядок за рядком з кінця файлу до початку. Це може бути корисно для аналізу лог-файлів, коли останні записи найважливіші."""


class ReverseFileIterator:
    """Iterator to read a file line by line in reverse order."""

    def __init__(self, filename):
        """Initialize with the filename"""
        self.filename = filename
        with open(filename, 'r', encoding='utf-8') as file:
            self.lines = file.readlines()
        self.index = len(self.lines) - 1

    def __iter__(self):
        """Return the iterator object"""
        return self

    def __next__(self):
        """Return the next line in reverse order"""
        if self.index < 0:
            raise StopIteration
        line = self.lines[self.index].strip()
        self.index -= 1
        return line


if __name__ == "__main__":
    # Create a test file
    with open("log.txt", "w", encoding="utf-8") as file:
        file.write("Log 1\nLog 2\nLog 3\nLog 4\nLog 5\nLog 6\nLog 7\nLog 8\nLog 9")

    # Iterate over file in reverse
    for line in ReverseFileIterator("log.txt"):

        print(line)
