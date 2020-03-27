def choose_question(next,last=0):
    num = 1
    if last == 1:
        num -= 1
    elif next == 1:
        num += 1
    return num
print(choose_question(next=1))