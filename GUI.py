from tkinter import *
import linecache
class GUI():

    def choose_question(self,last=0,next=0,num=1):
        if last==1:
            num-=1
        elif next==1:
            num+=1
        line = linecache.getline('./question', num)
        return line
    def text(self):
        text = Text(window, width=60, height=4)
        text.insert(INSERT, GUI.choose_question(self))
        text.pack()


    def radio(self):
        radio1 = Radiobutton(window, text='完全不同意', value=1).pack(anchor='w')
        radio2 = Radiobutton(window, text='不同意', value=2).pack(anchor='w')
        radio3 = Radiobutton(window, text='不确定', value=3).pack(anchor='w')
        radio4 = Radiobutton(window, text='同意', value=4).pack(anchor='w')
        radio5 = Radiobutton(window, text='完全同意', value=5).pack(anchor='w')
    def button(self):
        last_question_button = Button(window, text="上一题",command=GUI.choose_question(self,last=1,next=0))
        last_question_button.pack()
        next_question_button = Button(window, text="下一题",command=GUI.choose_question(self,last=0,next=1))
        next_question_button.pack()

if __name__=='__main__':
    window = Tk()
    window.title("性格测试")  # 窗口名
    width = 600
    height = 400
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(alignstr)  # 窗口大小
    window.resizable(width=False, height=True)  # 设置窗口是否可变

    gui=GUI()
    gui.text()
    gui.radio()
    gui.button()
    window.mainloop()


