#!/usr/bin/env python3

string = input("Введите строку:")

a = string.find("h")

b = string.rfind("h")

string1 = string[a+1:b]

string2 = string1.replace("h", "H")

c = ( string[:a+1]+ string2 + string[b:])

print("Результат: ",c)




