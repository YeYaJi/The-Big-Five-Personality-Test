# Python3中GUI图形界面构建

## 一.Tkinter

### 1.Tkinter介绍

介绍：Tkinter模块（Tk接口）是python的标准Tk GUI工具包的接口，通过内嵌在python解释器内部的Tcl解释器实现。先将Tkinter的调用转换成Tcl命令，然后交给Tcl解释器进行解释，实现python的GUI界面。

特点：（1）可用于windows/linux/unix/macintosh操作系统。

​              （2）使用简单，灵活性高。

​              （3）它是一个轻量级的跨平台图形用户界面开发工具。

### 2.Tkinter使用

（1）创建窗口

```
from tkinter import *
window = Tk()
window.title("性格测试")#窗口名
window.geometry('600x200')#窗口大小,可以随意制定
window.mainloop()
```

![1](/home/a/图片/1.png)

（2）添加文本控件

```
from tkinter import *
window = Tk()
window.title("性格测试")#窗口名
window.geometry('600x200')#窗口大小,可以随意制定

#添加文本控件

text=Text(window,width=60,height=4)#除了大小外，其他属性如背景颜色等见[网站](https://blog.csdn.net/weixin_42272768/article/details/100725243)。

text.insert(INSERT,'Hellow world')

text.pack()

window.mainloop()
```



![2](/home/a/图片/2.png)



（3）添加button控件

```
from tkinter import *
window = Tk()
window.title("性格测试")#窗口名
window.geometry('600x200')#窗口大小,可以随意制定

#添加文本控件

text=Text(window,width=60,height=4)
text.insert(INSERT,'hellow world')
text.pack()

def last_quesiton():
    text.delete(0.0,END)
    s1='last'
    text.insert(INSERT,s1)

last_question_button=Button(window,text="上一题",command=last_quesiton)
last_question_button.pack()

window.mainloop()
```

![3](/home/a/图片/3.png)

点击上一题后：

![2020-03-26 12-11-41 的屏幕截图](/home/a/图片/2020-03-26 12-11-41 的屏幕截图.png)

