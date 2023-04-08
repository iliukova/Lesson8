# Task 4
# Напишіть функцію, яка поверне кількість слів у текстовому рядку.

def words(text):
    return len(text.split())
print(words(input("Print some text: ")))