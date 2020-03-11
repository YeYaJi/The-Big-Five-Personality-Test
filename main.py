import sys

sys.path.append(r"/home/gsh/桌面/git1")
print(sys.path)
import functions as fc

##################################################################################

questions = open(r"/home/gsh/text-1", "r")
file_re_index = open(r"/home/gsh/re-index", "r")
file_every_index = open(r"/home/gsh/all-index", "r")
##################################################################################
grades = fc.show_question(questions)
grades = fc.alculate_reverse_score(file_re_index, grades)
grades_dict = fc.grade_covdict(grades)
file_every_index = slip_grade(file_every_index)

print(grades)
