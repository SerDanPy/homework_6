"""2. Ітератор для генерації унікальних ідентифікаторів
Створіть ітератор, який генерує унікальні ідентифікатори (наприклад, на основі UUID або хеш-функції). Ідентифікатори повинні генеруватися один за одним при кожній ітерації, і бути унікальними."""

import uuid


class UniqueIdIterator:
    """Iterator to generate unique UUID identifiers."""

    def __iter__(self):
        """Return the iterator object"""
        return self

    def __next__(self):
        """Generate and return a unique UUID"""
        return str(uuid.uuid4())


if __name__ == "__main__":
    id_iterator = UniqueIdIterator()
    count = int(input("Введіть к-сть потрібних ключів\n--->"))
    for i in range(count):

        print(next(id_iterator))
