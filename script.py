#!/usr/bin/python3

import math
from typing import List

TABLE_WIDTH = 5


# Заполняем таблицу по сообщению
def make_table(text: str) -> List[List[str]]:
    table = [[] for _ in range(math.ceil(len(text) / TABLE_WIDTH))]
    for i in range(len(text)):
        row = math.floor(i / TABLE_WIDTH)
        table[row].append(text[i])
    return table


def get_column_ids(key: int) -> range:
    column_ids = range(TABLE_WIDTH)
    # В зависимости от ключа меняем порядок считывания колонок
    if key % 2 == 0:
        column_ids = reversed(column_ids)
    return column_ids


def encrypt(text: str, key: int) -> str:
    result = ""
    table = make_table(text)
    column_ids = get_column_ids(key)
    for c in column_ids:
        rows = len(table)
        for r in range(rows):
            if c < len(table[r]):
                result += table[r][c]
    return result


def main() -> None:
    text = input("Введите текст: ")
    key = int(input("Введите ключ (целое число): "))

    result = encrypt(text, key)
    print(f"Зашифрованное сообщение: {result}")


if __name__ == "__main__":
    main()
