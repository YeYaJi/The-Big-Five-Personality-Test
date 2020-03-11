# 进行答题，返回输入的答案[list]
def show_question(file_path):
    questions = open(r"/home/gsh/text-1", "r")
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


def alculate_reverse_score(file_re_index, grades):
    re_index = [0]
    for index in file_re_index:
        re_index.append(int(index))
    for i in re_index:
        grades[i] = ~grades[i] + 1


def grade_covdict(grades):
    # 将grade转化为字典格式
    number = list(range(1, 241))
    enu = zip(number, grades)
    grades_dict = dict(enu)
    return grades_dict


def slip_sum_grade(file_every_index):
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
                index = int(string[i])
                f8_grade.append(grades_dict.get(index))
            f8_sum = sum(f8_grade)
            f8_sum_list.append(f8_sum)
            print(f8_sum)
            del f8_grade[:]
    return f8_sum_list


def add_all_grades(f8_sum_list):
    N = sum(f8_sum_list[0:6])
    E = sum(f8_sum_list[6:12])
    O = sum(f8_sum_list[12:18])
    A = sum(f8_sum_list[18:24])
    C = sum(f8_sum_list[24:30])
    all_grades = [N, E, O, A, C]
    all_grades.extend(f8_sum_list)
    return all_grades
