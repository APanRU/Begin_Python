# Задача 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять
# количество вхождений одной строки в другой. Нельзя юзать find или count.

# def words_count(text1, text2):
#     return text1.count(text2)


# print(Words_count(text1=input(), text2=input()))


def str_count_two(text1, text2):
    count = 0
    for x in range(len(text1) - len(text2) + 1):
        if text1[x:x+len(text2)] == text2:
            count += 1
    return count


print(str_count_two(text1=input("Введите первый текст: "),
      text2=input("Введите второй текст: ")))
