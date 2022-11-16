from easygui import *
from viev_gui import *


def choices_menu_gui():
    msg = "Хотите продолжить работу с программой?"
    choices = ["Да", "Нет"]
    if ynbox(msg, choices):
        print("test")  # возврат к основному меню def menu
    else:
        print ("Спасибо, что воспользовались нашей программой!")


def choices_log_gui():
    viev_result_gui()
    msg = "Хотите увидеть историю операций?"
    title = "Выбор"
    choices = ["Да", "Нет"]
    if ynbox(msg, title, choices):
    # viev_log_gui()
        viev_log_text_gui()
        choices_menu_gui()         
    else:
        choices_menu_gui()


# try:

#     a = str.lower(input("Хотите посмотреть историю вычислений (Да/Нет): "))
#     if a == "да":
#         print(viev_log())
#         b = str.lower(input("Хотите продолжить работу с программой (Да/Нет): "))
#         if b == "да":
#             # возврат к основному меню def menu

#     else:
#         b = str.lower(input("Хотите продолжить работу с программой (Да/Нет): "))
# except:
#     print("Введены некорректные данные!")
