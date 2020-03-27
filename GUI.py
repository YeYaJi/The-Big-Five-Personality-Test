import tkinter as tk
import linecache
#import logistic_class as logis

class GUI():
    def __init__(self, num, grads):
        self.num = num
        self.window = tk.Tk()
        self.window.title("性格测试")  # 窗口名
        self.grads=grads
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
        #print(self.num)
        return line

    def show_text(self, question):
        self.text.delete(0.0,"end")
        self.text.insert(tk.INSERT, question)
        self.text.pack()

    def click_radio0(self):
        self.grads[1]=0
        print(self.grads)
    def click_radio1(self):

        print(self.grads)

    def click_radio2(self):

        print(self.grads)

    def click_radio3(self):

        print(self.grads)

    def click_radio4(self):

        print(self.grads)

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
        self.show_text("start test")
        self.radio()
        self.button()

    def show_next_question(self):
        question_text = self.choose_question(0, 1)
        self.show_text(question_text)

    def show_prev_question(self):
        question_text = self.choose_question(1, 0)
        self.show_text(question_text)

    def run(self):
        self.draw_window()
        self.window.mainloop()

if __name__=='__main__':
    gui_ins = GUI(0,{})
    gui_ins.run()


