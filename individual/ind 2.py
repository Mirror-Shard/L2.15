#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Написать программу, которая будет удалять все комментарии из исходного файла
с кодом на языке Python. Пройдите по всем строкам в файле на предмет поиска
символа #. Обнаружив его, программа должна удалить все содержимое,
начиная с этого символа и до конца строки.
"""


if __name__ == "__main__":

    # Запрос имени файла
    file_name = input("Введите имя файла, который нужно открыть: ")

    # Разбивает на строки первый файл
    with open(file_name, "r") as file:
        content = file.readlines()

    # Запрос имени для нового файла
    new_file_name = input("Введите имя для нового файла: ")

    # Создаёт новый файл
    with open(new_file_name, "w") as new_file:
        # Вписывает строки которые не начинаются с #
        for line in content:
            if not line.startswith('#'):
                new_file.write(line)