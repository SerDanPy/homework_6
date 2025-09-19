"""5. Генератор для створення нескінченної послідовності
Створіть генератор, який генерує нескінченну послідовність парних чисел. Використайте менеджер контексту для обмеження кількості генерованих чисел до 100 і збереження їх у файл."""

from contextlib import contextmanager


@contextmanager
def limit_generator(generator, limit):
    #Context manager to limit the number of generated items
    count = 0
    iterator = iter(generator)
    try:
        def limited_gen():
            nonlocal count
            while count < limit:
                yield next(iterator)
                count += 1
        yield limited_gen()
    except StopIteration:
        pass


def even_numbers():
    num = 0
    while True:
        yield num
        num += 2


if __name__ == "__main__":
    #First 100 numbers to file
    with open("even_numbers.txt", "w", encoding="utf-8") as file:
        with limit_generator(even_numbers(), 100) as limited:
            for num in limited:
                file.write(f"{num}\n")
                print(num, end=" ")