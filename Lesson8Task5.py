# Task 5
# Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат.
# Наприклад:
# > 123,34
# > one hundred twenty three dollars thirty four cents

import num2word
def num_in_words(price_num):
    dollar, cent = price_num.split('.')
    result = f'{num2word.word(dollar).lower()} dollars ' \
             f'{num2word.word(cent).lower()} cents'
    return result


price = str(input('price = ').replace(',', '.'))

print(num_in_words(price))