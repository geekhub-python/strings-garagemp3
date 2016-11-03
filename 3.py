#!/usr/bin/env python3

string = input("Введите строку:")

a = string[len(string) // 2 + len(string) % 2:]

b = string[:len(string) // 2 + len(string) % 2]

print("Новая строка: ",a + b)

