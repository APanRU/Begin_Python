# Задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (здесь только буквы).
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open(r'Begin_Python\Homework\Homework_5\Task_2\text_words.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст для сжатия: '))
with open(r'Begin_Python\Homework\Homework_5\Task_2\text_words.txt', 'r') as file:
    my_txt = file.readline()
    txt_compr = my_txt.split()

print(my_txt)


def file_encod(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond


txt_compr = file_encod(my_txt)

with open(r'Begin_Python\Homework\Homework_5\Task_2\text_code_words.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_compr}')
print(txt_compr)