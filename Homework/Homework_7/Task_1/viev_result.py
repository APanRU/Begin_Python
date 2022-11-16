
def viev_result():
    with open(r"Begin_Python\Homework\Homework_7\Task_1\log.txt", 'r') as file:
        lst = list(file.readlines())
        lastline = lst[len(lst)-1]
        return lastline


print(viev_result())




# # Open the file
# myfile = open("filename.txt", "r")
# # Read all the lines into a List
# lst = list(myfile.readlines())
# # Close the file
# myfile.close()
# # Get just the last line
# lastline = lst[len(lst)-1]
# # Locate the start of the label you want, 
# # and set the start position at the end 
# # of the label:
# intStart = lastline.find('location="') + 10
# # snip off a substring from the 
# # target value to the end (this is called a slice):
# sub = lastline[intStart:]
# # Your ending marker is now the 
# # ending quote (") that is located 
# # at the end of your target value.
# # Get it's index.
# intEnd = sub.find('"')
# # Finally, grab the value, using 
# # another slice operation.
# finalvalue = sub[0:intEnd]
# print finalvalue


# try:
#     a = str.lower(input("Хотите посмотреть историю вычислений (Да/Нет): "))
#     if a == "да":
#         print(viev_log())
#     else:
#         b = str.lower(
#             input("Хотите продолжить работу с программой (Да/Нет): "))
# except:
#     print("Введены некорректные данные!")