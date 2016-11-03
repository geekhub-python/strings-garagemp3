#!/usr/bin/env python3

string = input("Введите строку: ")

a = string.find ("f")
b = string.rfind("f")

if a == b >= 0 :

    print(" Индекс f : ", a)

elif a != b :

    print("Первый индекс f в строке: ", a)

    print("Последний индекс f в строке: ", b)
