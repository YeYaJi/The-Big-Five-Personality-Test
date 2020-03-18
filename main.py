import sys
import functions as fc

##################################################################################
sys.path.append(r"./")  # functions.py的path
####################################################################################
questions = open(r"./text-1", "r")  # 读取题目
file_re_index = open(r"./re-index", "r")  # 读取反向索引
file_every_index = open(r"./all-index", "r")  # 依次分行读取每个大维度下的小维度索引：第一行=注释,第二行=n1~n6,第三行=注释,第四行=c1~c6,…………,
##################################################################################
grades = fc.show_question(questions)  # 得到所有输入的分数

grades = fc.alculate_reverse_score(file_re_index, grades)  # 把反向的分数取负
grades_dict = fc.grade_covdict(grades)  # 分数转化为字典格式{key=index：value=grades}
f8_sum_list = fc.slip_sum_grades(file_every_index, grades_dict)  # 得到每个大维度下的小维度分数之和
all_grades = fc.add_all_grades(f8_sum_list)  # 得到全部的分数[N,E,O,A,C,N1~N6,E1~E6,…………]
really_grade = fc.calculation_really_grades(all_grades)  # 根据计算法则得出最后的分数
fc.print_grades(really_grade)  # 打印分数
