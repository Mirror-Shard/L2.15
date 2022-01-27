#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Написать программу, которая считывает текст из файла и выводит на экран
только строки не содержащие двухзначных чисел.
"""


if __name__ == "__main__":

    # Открытие файла
    with open("text.txt", 'r', encoding="utf-8") as file:
        content = file.readlines()

        # Проходит по строкам
        for line in content:
            words = line.split()
            # Проходит по словам
            for word in words:
                # Печатает строку, если в ней 2-х значное число
                if word.isdigit() and len(word) == 2:
                    print(line)
