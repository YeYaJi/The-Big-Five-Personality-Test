import tkinter as tk
import linecache

class GUI():
    global grades
    grades = {}
    global question_num
    question_num=1
    def __init__(self, num):
        self.num = num
        self.window = tk.Tk()
        self.window.title("性格测试")  # 窗口名
        self.first_question = linecache.getline('./question', 1)
        width = 600
        height = 400
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)  # 窗口大小
        self.window.resizable(width=False, height=True)  # 设置窗口是否可变

    def choose_question(self, last=0, next=0):
        if last == 1:
            self.num -= 1
        elif next == 1:
            self.num += 1
        line = linecache.getline('./question', self.num)
        return line

    def show_text(self, question):
        self.text.delete(0.0, "end")
        self.text.insert(tk.INSERT, question)
        self.text.pack()

    def click_radio0(self):
        grades[question_num] = 0
        print(grades)

    def click_radio1(self):
        grades[question_num] = 1
        #print(grades)
    def click_radio2(self):
        grades[question_num] = 2
        #print(grades)

    def click_radio3(self):
        grades[question_num] = 3
        #print(grades)

    def click_radio4(self):
        grades[question_num] = 4
        #print(grades)

    def radio(self):
        r = tk.IntVar()
        self.radio1 = tk.Radiobutton(self.window, text='完全不同意', variable=r, command=self.click_radio0).pack(anchor='w')
        self.radio2 = tk.Radiobutton(self.window, text='不同意', variable=r, value=1, command=self.click_radio1).pack(anchor='w')
        self.radio3 = tk.Radiobutton(self.window, text='不确定', variable=r, value=2, command=self.click_radio2).pack(anchor='w')
        self.radio4 = tk.Radiobutton(self.window, text='同意', variable=r, value=3, command=self.click_radio3).pack(anchor='w')
        self.radio5 = tk.Radiobutton(self.window, text='完全同意', variable=r, value=4, command=self.click_radio4).pack(anchor='w')

    def button(self):

        self.last_question_button = tk.Button(self.window, text="上一题", command=self.show_prev_question)
        self.last_question_button.pack()
        self.next_question_button = tk.Button(self.window, text="下一题", command=self.show_next_question)
        self.next_question_button.pack()



    def draw_window(self):
        self.text = tk.Text(self.window, width=60, height=4)
        #self.show_text('start test')
        self.show_text(linecache.getline('./question', 1))
        self.radio()
        self.button()



    def show_next_question(self):
        if question_num not in grades.keys():
            warring_window = tk.Tk()
            warring_window.title("提示")
            warring_text = tk.Label(warring_window, text="请点击上一题,回答第"+str(question_num)+"题")
            width = 300
            height = 150
            screenwidth = warring_window.winfo_screenwidth()
            screenheight = warring_window.winfo_screenheight()
            alignstr1 = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            warring_window.geometry(alignstr1)  # 窗口大小
            warring_text.pack()
            #grades[self.question_num]=-1  #错过某题没有回答，该题答案为-1，表示异常
            #print("请点击上一题,回答第"+str(self.question_num)+"题")
        else:
            question_num += 1

    def show_prev_question(self):
        question_text = self.choose_question(1, 0)
        question_num -= 1
        self.show_text(question_text)



    def run(self):
        self.draw_window()
        self.window.mainloop()





class Score_caculate():
    # 计算反向分数
    def alculate_reverse_score(self, file_re_index):
        re_index = []
        for index in file_re_index:
            re_index.append(int(index))
        for i in re_index:
            grades[i] = 4-grades[i]

    # 得到每个大维度下的小维度分数之和
    def slip_sum_grades(self, file_every_index):
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
                    f8_grade.append(grades.get(index))
                f8_sum = sum(f8_grade)
                f8_sum_list.append(f8_sum)

                del f8_grade[:]
        return f8_sum_list

    # 得到全部的分数[N,E,O,A,C,N1~N6,E1~E6,…………]
    def add_all_grades(self, f8_sum_list):
        N = sum(f8_sum_list[0:6])
        E = sum(f8_sum_list[6:12])
        O = sum(f8_sum_list[12:18])
        A = sum(f8_sum_list[18:24])
        C = sum(f8_sum_list[24:30])
        all_grades = [N, E, O, A, C]
        all_grades.extend(f8_sum_list)
        return all_grades

    # 根据计算法则得出最后的分数
    def calculation_really_grades(self,all_grades):
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
    def print_grades(self,really_grade):
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
if __name__=='__main__':
    gui_ins = GUI(1)
    gui_ins.run()
    file_re_index = open(r"./re-index", "r")
    file_every_index = open(r"./all-index", "r")
    score = Score_caculate()
    score.alculate_reverse_score(file_re_index)
    score_slip_sum_grades = score.slip_sum_grades(file_every_index)
    score_add_all_grades = score.add_all_grades(score_slip_sum_grades)
    score_calculation_really_grades=score.calculation_really_grades(score_add_all_grades)
    #score.print_grades(score_calculation_really_grades)






