# 进行答题，返回输入的答案[list]
def show_question(questions):
    for i, sentience in enumerate(questions):
        print("第%d题\n" % (i + 1))
        print(sentience)
        print("请输入分数1～5")
        grade_in = input(":")
        grades = Judgement_input(grade_in)
    return grades


# 判断输入异常
def Judgement_input(grade_in):
    grades = [0]
    cord = [1, 2, 3, 4, 5]
    while 1:
        if grade_in.isdigit():

            grade = int(grade_in)
            if grade in cord:
                grades.append(grade)
                break
            else:
                print("请确认数字的大小")
                grade_in = input(":")
        else:
            print("请输入数字")
            grade_in = input(":")
    return grades

# 把反向的分数取负
def alculate_reverse_score(file_re_index, grades):
    re_index = [0]
    for index in file_re_index:
        re_index.append(int(index))
    for i in re_index:
        grades[i] = ~grades[i] + 1
    return grades

# 分数转化为字典格式{key=index：value=grades}
def grade_covdict(grades):
    # 将grade转化为字典格式
    number = list(range(1, 241))
    enu = zip(number, grades)
    grades_dict = dict(enu)
    return grades_dict

# 得到每个大维度下的小维度分数之和
def slip_sum_grades(file_every_index, grades_dict):
    all_index = []
    every_6_index = []
    f8_grade = []
    f8_sum_list = []
    for f in file_every_index:
        all_index.append(f)

    for m in range(5):
        every_6_index.append(all_index[1 + (m * 12):12 + (m * 12):2])

        for z in range(6):

            string_ever_8 = every_6_index[m][z].split(sep='.')

            for i in range(len(string_ever_8)):
                index = int(string_ever_8[i])
                f8_grade.append(grades_dict.get(index))
            f8_sum = sum(f8_grade)
            f8_sum_list.append(f8_sum)

            del f8_grade[:]
    return f8_sum_list

# 得到全部的分数[N,E,O,A,C,N1~N6,E1~E6,…………]
def add_all_grades(f8_sum_list):
    N = sum(f8_sum_list[0:6])
    E = sum(f8_sum_list[6:12])
    O = sum(f8_sum_list[12:18])
    A = sum(f8_sum_list[18:24])
    C = sum(f8_sum_list[24:30])
    all_grades = [N, E, O, A, C]
    all_grades.extend(f8_sum_list)
    return all_grades

# 根据计算法则得出最后的分数
def calculation_really_grades(all_grades):
    man_M = [83.78, 109.96, 110.64, 113, 123.88, 14.15, 13.82, 14.37, 15.35, 14.86, 11.23,
             21.53, 18.69, 15.1, 18.33, 17.24, 19.07, 15.19,
             20.7, 19.47, 15.02, 19.62, 20.64, 21.07, 19.03, 20.99, 15.33, 16.67, 19.91,
             20.8, 18.39, 23.47, 20.02, 20.48, 20.72]

    man_SD = [24.41, 18.27, 15.88, 14.9, 20.32, 5.7, 5.24, 5.7, 4.73, 4.88,
              5.09, 4.27, 4.65, 4.37, 4.74, 4.64, 4.85,
              4.19, 4.88, 3.95, 3.61, 4.98, 3.97,
              3.94, 5.11, 3.53, 4.64, 4.06, 3.59,
              4.34, 4.21, 4.22, 4.34, 4.66, 4.63]
    really_grade = []
    f8_sum_list = all_grades
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
        elif (f8_sum_list[i] > man_M[i] + 0.3 * man_SD[i]) and (f8_sum_list[i] <= man_M[i] + 0.6 * man_SD[i]):
            really_grade.append(7)
        elif (f8_sum_list[i] > man_M[i] + 0.6 * man_SD[i]) and (f8_sum_list[i] <= man_M[i] + man_SD[i]):
            really_grade.append(8)
        elif (f8_sum_list[i] > man_M[i] + man_SD[i]) and (f8_sum_list[i] <= man_M[i] + 1.5 * man_SD[i]):
            really_grade.append(9)
        elif (f8_sum_list[i] > man_M[i] + 1.5 * man_SD[i]):
            really_grade.append(10)

    return really_grade

# 打印分数
def print_grades(really_grade):
    print("N =", really_grade[0])
    print("E =", really_grade[1])
    print("O =", really_grade[2])
    print("A =", really_grade[3])
    print("C =", really_grade[4])
    print("N1 =", really_grade[5])
    print("N2 =", really_grade[6])
    print("N3 =", really_grade[7])
    print("N4 =", really_grade[8])
    print("N5 =", really_grade[9])
    print("N6 =", really_grade[10])
    print("E1 =", really_grade[11])
    print("E2 =", really_grade[12])
    print("E3 =", really_grade[13])
    print("E4 =", really_grade[14])
    print("E5 =", really_grade[15])
    print("E6 =", really_grade[16])
    print("O1 =", really_grade[17])
    print("O2 =", really_grade[18])
    print("O3 =", really_grade[19])
    print("O4 =", really_grade[20])
    print("O5 =", really_grade[21])
    print("O6 =", really_grade[22])
    print("A1 =", really_grade[23])
    print("A2 =", really_grade[24])
    print("A3 =", really_grade[25])
    print("A4 =", really_grade[26])
    print("A5 =", really_grade[27])
    print("A6 =", really_grade[28])
    print("C1 =", really_grade[29])
    print("C2 =", really_grade[30])
    print("C3 =", really_grade[31])
    print("C4 =", really_grade[32])
    print("C5 =", really_grade[33])
    print("C6 =", really_grade[34])
