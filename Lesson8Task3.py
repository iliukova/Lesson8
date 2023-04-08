# Task 3
# Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел.
# Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».

def find_elem(list_of_nums, user_search):
    for item, element in enumerate(list_of_nums):
        if element == user_search:
            return item
    return -1


list_of_nums = [10, 20, 30, 40, 50, 60, 70, 80]
user_search = int(input('Print number: '))
print(find_elem(list_of_nums, user_search))