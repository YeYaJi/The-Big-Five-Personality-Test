from tkinter import *
window = Tk()

window.title("性格测试")#窗口名
width=600
height=500
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
window.geometry(alignstr)#窗口大小
window.resizable(width=False,height=True)#设置窗口是否可变

text=Text(window,width=60,height=4)
text.insert(INSERT,"第一题")
text.pack()
radio1=Radiobutton(window,text='完全不同意',value=1).pack()
radio2=Radiobutton(window,text='不同意',value=2).pack()
radio3=Radiobutton(window,text='不确定',value=3).pack()
radio4=Radiobutton(window,text='同意',value=4).pack()
radio5=Radiobutton(window,text='完全同意',value=5).pack()
window.mainloop()
