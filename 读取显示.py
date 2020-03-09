# 显示答题，保存答案
# str = open(r"/home/gsh/text-1", "r")
# grades = [0]
# for i, sentience in enumerate(str):
#     print("第%d题\n" % (i + 1))
#     print(sentience)
#     print("请输入分数1～5")
#     while 1:
#         cord = [1, 2, 3, 4, 5]
#
#         g_in = input(":")
#
#         if g_in.isdigit():
#             grade = int(g_in)
#             if grade in cord:
#                 grades.append(grade)
#                 break
#             else:
#                 print("请输入正确大小的数字_2")
#
#         else:
#             print("请输入正确大小的数字_1")
#
# print(grades)
grades = [3] * 240
print(grades)
# 计算分数
ind = open(r"/home/gsh/re-index", "r")
re_index = [0]
for f_index in ind:
    f_index = int(f_index)
    re_index.append(f_index)
print(re_index)

for i in re_index:
    grades[i] = ~grades[i] + 1
print(grades)
Total_score = sum(grades)
print(Total_score)

# 依次存入各个维度的索引
f = open(r"/home/gsh/all-index", "r")
all_index = []
n = []
for f1 in f:
    all_index.append(f1)

for m in range(5):
    n.append(all_index[1 + (m * 12):12 + (m * 12):2])

    print('n[m]====')
    print(n[m])
    print("__________________________________________________")
print(len(n))
for z in range(6):
    string = n[z]
    # string = string.split(sep='.')
    print('string======')
    print(string)
#
#     ########################################
#     for i in range(len(string)):
#         index = int(string[i])
#         print(index)
