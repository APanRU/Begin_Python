# 1. Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную
# сплошную возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример: *
# [1, 5, 2, 3, 4, 6, 1, 7] = >  [1, 7]
# [1, 5, 2, 3, 4,  1, 7] = >  [1, 5]

nums = [1, 5, 2, 3, 4, 6, 1, 7]
nums2 = [1, 5, 2, 3, 4,  1, 7]


def find_list(start_num, current_list):
    new_list = [start_num]
    max_num = max(current_list)

    for k in range(start_num, max_num):
        if start_num + 1 in current_list:
            new_list.append(start_num + 1)
            start_num += 1

    if len(new_list) > 1:
        return new_list

    return []


try:
    list_of_numders = [1, 5, 3, 4,2,  1, 7]
    lists = []

    min_num = min(list_of_numders)

    current_list = find_list(min_num, list_of_numders)

    print(current_list)


except:
    print("Введены некоректные данные!")


# def get_up2(nums):
#     ups = [nums[0]]
#     for i in nums:
#         if i > max(ups):
#             ups.append(i)
#     return ups


# print(get_up2(nums))
# print(get_up2(nums2))


# def get_up(nums):
#     ups = []
#     for i in range(len(nums)):
#         if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
#             ups.append(nums[i])
#     return ups


# print(get_up(nums))
# print(get_up(nums2))
