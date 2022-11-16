from easygui import *
from viev_log import viev_log
from viev_result import viev_result


def viev_result_gui():
    title = "Вывод результата. "
    button = " OK "
    msgbox(viev_result(), title, button)


def viev_log_gui():
    title = "История операций. "
    button = " OK "
    msgbox(viev_log(), title, button)


def viev_log_text_gui():
    filename = "Begin_Python\Homework\Homework_7\Task_1\log.txt"
    f = open(filename, 'r')
    content = f.readlines()
    f.close()
    codebox(filename, 'История операций', content)


