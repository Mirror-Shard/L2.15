#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Создайте простой файловый менеджер, который может создавать, удалять,
перемещать, переименовывать и совершать другие операции с файлами и папками.
"""

import os


if __name__ == "__main__":

    print("Для работы с файлами вводите: *команда* *имя_файла*")
    print("Список команд - cd, ls, getcwd\n"
          "mkdir, mkfile, remove, rmdir, rename")

    while True:

        # Бесконечный запрос сообщения
        message = (input(">>> ").lower()).split()

        # Делит на команду или команду и имя_файла
        if len(message) == 1:
            command = message[0]
        elif len(message) == 2:
            command, file_name = message[0], message[1]
        else:
            print("Неверное количество аргументов")
            continue

        # Создаёт папку
        if command == "mkdir":
            os.mkdir(file_name)

        # Создаёт файл
        elif command == "mkfile":
            new_file = open(file_name, 'w')

        # Показывает путь к текущей директории
        elif command == "getcwd":
            print(os.getcwd())

        # Кнопка "Назад"
        elif command == "..":
            print(os.chdir(".."))
            print(os.getcwd())

        # Показывает список папок и файлов в текущем каталоге
        elif command == "ls":
            print(os.listdir())

        # Переход в другую директорию
        elif command == "cd":
            os.chdir(file_name)
            print(os.getcwd())

        # Удаляет файл
        elif command == "remove":
            os.remove(file_name)

        # Удаляет папку
        elif command == "rmdir":
            os.rmdir(file_name)

        # Переименовывает файл или каталог
        elif command == "rename":
            new_name = input("Введите новое имя: ")
            os.rename(file_name, new_name)

        # Помощь
        elif command == "help":
            print("Для работы с файлами вводите: *команда* *имя_файла*")
            print("Список команд - cd, ls, getcwd\n"
                  "mkdir, mkfile, remove, rmdir, rename")

        else:
            print("Неверная команда")
