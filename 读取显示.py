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
# 把反向的分数取反
ind = open(r"/home/gsh/re-index", "r")
re_index = [0]
for f_index in ind:
    f_index = int(f_index)
    re_index.append(f_index)
print(re_index)

for i in re_index:
    grades[i] = ~grades[i] + 1
print(grades)
# 将grade转化为字典格式
number = list(range(1, 241))
enu = zip(number, grades)
grades_dict = dict(enu)
print((grades_dict))

# 依次存入各个维度的索引
f = open(r"/home/gsh/all-index", "r")
all_index = []
n = []
f8_index = []
f8_grade = []
f_sum_g = []
f8_zongfen = 0
f8_sum_list = []
for ff in f:
    all_index.append(ff)

for m in range(5):
    n.append(all_index[1 + (m * 12):12 + (m * 12):2])

    # print('n[%d]====' % m)
    # print(n[m])print(f8_sum)
    # print("__________________________________________________")

    for z in range(6):
        string = n[m][z]
        string = string.split(sep='.')
        # print('string======')
        # print(string)
        ########################################
        for i in range(len(string)):
            index = int(string[i])
            # print(index)
            # f8_index.append(index)
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

            f8_grade.append(grades_dict.get(index))
        f8_sum = sum(f8_grade)
        f8_sum_list.append(f8_sum)
        print(f8_sum)
        del f8_grade[:]
print(f8_sum_list)

N = sum(f8_sum_list[0:6])
E = sum(f8_sum_list[6:12])
O = sum(f8_sum_list[12:18])
A = sum(f8_sum_list[18:24])
C = sum(f8_sum_list[24:30])
shou = [N, E, O, A, C]

shou.extend(f8_sum_list)
f8_sum_list=shou
# del f8_index[:]
###################################################
# 得到最后的30个分数

man_M = [83.78, 109.96, 110.64, 113, 123.88, 14.15, 13.82, 14.37, 15.35, 14.86, 11.23,
         21.53, 18.69, 15.1, 18.33, 17.24, 19.07, 15.19,
         20.7, 19.47, 15.02, 19.62, 20.64, 21.07, 19.03, 20.99, 15.33, 16.67, 19.91,
         20.8, 18.39, 23.47, 20.02, 20.48, 20.72]

man_SD = [24.41, 18.27, 15.88, 14.9, 20.32, 5.7, 5.24, 5.7, 4.73, 4.88,
          5.09, 4.27, 4.65, 4.37, 4.74, 4.64, 4.85,
          4.19, 4.88, 3.95, 3.61, 4.98, 3.97,
          3.94, 5.11, 3.53, 4.64, 4.06, 3.59,
          4.34, 4.21, 4.22, 4.34, 4.66, 4.63]

####################################################
really_grade = []
for i in range(35):

    if f8_sum_list[i] < man_M[i] - 2 * man_SD[i]:
        really_grade.append(1)
    elif (f8_sum_list[i] >= man_M[i] - 2 * man_SD[i]) and (f8_sum_list[i] <= man_M[i] - 1.5 * man_SD[i]):
        really_grade.append(2)
    elif ((f8_sum_list[i] > man_M[i] - 1.5 * man_SD[i])) and (f8_sum_list[i] <= man_M[i] - man_SD[i]):
        really_grade.append(3)
    elif (f8_sum_list[i] > man_M[i] - man_SD[i]) and (f8_sum_list[i] <= man_M[i] - 0.5 * man_SD[i]):
        really_grade.append(4)
    elif (f8_sum_list[i] > man_M[i] - 0.5 * man_SD[i]) and (f8_sum_list[i] <= man_M[i]):
        really_grade.append(5)
    elif (f8_sum_list[i] > man_M[i]) and (f8_sum_list[i] <= man_M[i] + 0.3 * man_SD[i]):
        really_grade.append(6)
    elif (f8_sum_list[i] > N_man_M[i] + 0.3 * man_SD[i]) and (f8_sum_list[i] <= man_M[i] + 0.6 * man_SD[i]):
        really_grade.append(7)
    elif (f8_sum_list[i] > man_M[i] + 0.6 * man_SD[i]) and (f8_sum_list[i] <= man_M[i] + man_SD[i]):
        really_grade.append(8)
    elif (f8_sum_list[i] > man_M[i] + man_SD[i]) and (f8_sum_list[i] <= man_M[i] + 1.5 * man_SD[i]):
        really_grade.append(9)
    elif (f8_sum_list[i] > man_M[i] + 1.5 * man_SD[i]):
        really_grade.append(10)
print(really_grade)
print(len(f8_sum_list))
