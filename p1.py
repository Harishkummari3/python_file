list1 = [1, 2, 3, 4, 5, 4]
# for i in list1:
#     if i == 4:
#         list1.remove(i)
# print(list1)
list2 = [i for i in list1 if i != 4]
print(list2)
