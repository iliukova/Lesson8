# Task 1
# Реалізуйте функцію, параметрами якої є два числа та рядок.
# Повертає вона конкатенацію рядка із сумою чисел.

def conc(a, b, text):
    return f'{int(a)+int(b)}{text}'

print(conc(a= input("print a: "), b = input("print b: ") , text = input("print text: ")))
