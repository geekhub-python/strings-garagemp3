#!/usr/bin/env python3

string = input("Введите строку: ")

a = string.find("")

word1 = string[:a]

word2 = string[a:]

string2 = word2 + " " + word1

print("Результат:",string2)
