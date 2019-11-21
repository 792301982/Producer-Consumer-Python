from tkinter import *

root = Tk()
root.title('生产者消费者 By Yangning')
root.geometry('400x400')

Label(root, text='缓冲区：', bg='red',
      width=10, height=2).grid(row=1, column=1)
huanchong_text_list = [StringVar(), StringVar()]
Label(root, textvariable=huanchong_text_list[0], bg='green',
      width=10, height=2).grid(row=1, column=2)
Label(root, textvariable=huanchong_text_list[1], bg='green',
      width=10, height=2).grid(row=1, column=3)

Label(root, text='阻塞队列：', bg='yellow',
      width=10, height=2).grid(row=2, column=1)
zuse_text_list = [StringVar(), StringVar(), StringVar(), StringVar()]
Label(root, textvariable=zuse_text_list[0], bg='green', width=10, height=2).grid(
    row=2, column=2)
Label(root, textvariable=zuse_text_list[1], bg='green', width=10, height=2).grid(
    row=2, column=3)
Label(root, textvariable=zuse_text_list[2], bg='green', width=10, height=2).grid(
    row=2, column=4)


Label(root, text='等待队列：', bg='red',
      width=10, height=2).grid(row=3, column=1)
wait_text_list = [StringVar(), StringVar(), StringVar(), StringVar()]
Label(root, textvariable=wait_text_list[0], bg='green', width=10, height=2).grid(
    row=3, column=2)
Label(root, textvariable=wait_text_list[1], bg='green', width=10, height=2).grid(
    row=3, column=3)
Label(root, textvariable=wait_text_list[2], bg='green', width=10, height=2).grid(
    row=3, column=4)


huanchong_list = list()
zuse_list = list()
wait_list = list()



def qingkong(x):
    for i in x:
        i.set('')


def charu(x, l):
    for n, i in enumerate(l):
        x[n].set(i)


def check_zuse():
    if '生产者1' in zuse_list or len(zuse_list)>=3:
        Button(root, text='生产者1', width=10, height=1,
               state=DISABLED).grid(row=4, column=1)
    if '生产者2' in zuse_list or len(zuse_list)>=3:
        Button(root, text='生产者2', width=10, height=1,
               state=DISABLED).grid(row=4, column=2)
    if '生产者3' in zuse_list or len(zuse_list)>=3:
        Button(root, text='生产者3', width=10, height=1,
               state=DISABLED).grid(row=4, column=3)
    if '生产者4' in zuse_list or len(zuse_list)>=3:
        Button(root, text='生产者4', width=10, height=1,
               state=DISABLED).grid(row=4, column=4)


def check_wait():
    if '消费者1' in wait_list or len(wait_list)>=3:
        Button(root, text='消费者1', width=10, height=1,
               state=DISABLED).grid(row=5, column=1)
    if '消费者2' in wait_list or len(wait_list)>=3:
        Button(root, text='消费者2', width=10, height=1,
               state=DISABLED).grid(row=5, column=2)
    if '消费者3' in wait_list or len(wait_list)>=3:
        Button(root, text='消费者3', width=10, height=1,
               state=DISABLED).grid(row=5, column=3)
    if '消费者4' in wait_list or len(wait_list)>=3:
        Button(root, text='消费者4', width=10, height=1,
               state=DISABLED).grid(row=5, column=4)

def refresh_button():
    #刷新按钮
    Button(root, text='生产者1', width=10, height=1,
           command=lambda: shengchan(1)).grid(row=4, column=1)
    Button(root, text='生产者2', width=10, height=1,
           command=lambda: shengchan(2)).grid(row=4, column=2)
    Button(root, text='生产者3', width=10, height=1,
           command=lambda: shengchan(3)).grid(row=4, column=3)
    Button(root, text='生产者4', width=10, height=1,
           command=lambda: shengchan(4)).grid(row=4, column=4)
    Button(root, text='消费者1', width=10, height=1,
           command=lambda: xiaofei(1)).grid(row=5, column=1)
    Button(root, text='消费者2', width=10, height=1,
           command=lambda: xiaofei(2)).grid(row=5, column=2)
    Button(root, text='消费者3', width=10, height=1,
           command=lambda: xiaofei(3)).grid(row=5, column=3)
    Button(root, text='消费者4', width=10, height=1,
           command=lambda: xiaofei(4)).grid(row=5, column=4)

def shengchan(number):
    global huanchong_list, wait_list, zuse_list
    
    if(len(wait_list) !=0):
        wait_list=wait_list[1:]
    else:
        if(len(huanchong_list) < 2):
            huanchong_list.append('生产者%s' % number)
        else:
            zuse_list.append('生产者%s' % number)

    qingkong(huanchong_text_list)
    qingkong(wait_text_list)
    qingkong(zuse_text_list)
    charu(huanchong_text_list, huanchong_list)
    charu(wait_text_list, wait_list)
    charu(zuse_text_list, zuse_list)
    refresh_button()
    check_zuse()
    check_wait()


Button(root, text='生产者1', width=10, height=1,
       command=lambda: shengchan(1)).grid(row=4, column=1)
Button(root, text='生产者2', width=10, height=1,
       command=lambda: shengchan(2)).grid(row=4, column=2)
Button(root, text='生产者3', width=10, height=1,
       command=lambda: shengchan(3)).grid(row=4, column=3)
Button(root, text='生产者4', width=10, height=1,
       command=lambda: shengchan(4)).grid(row=4, column=4)


def xiaofei(number):
    global huanchong_list, wait_list, zuse_list
    if(len(huanchong_list) != 0):
        huanchong_list = huanchong_list[1:]
        if(len(zuse_list) != 0):
            huanchong_list.append(zuse_list[0])
            zuse_list = zuse_list[1:]
    else:
        wait_list.append('消费者%s' % number)

    qingkong(huanchong_text_list)
    qingkong(wait_text_list)
    qingkong(zuse_text_list)
    charu(huanchong_text_list, huanchong_list)
    charu(wait_text_list, wait_list)
    charu(zuse_text_list, zuse_list)
    refresh_button()
    check_zuse()
    check_wait()


#布置消费者按钮
Button(root, text='消费者1', width=10, height=1,
       command=lambda: xiaofei(1)).grid(row=5, column=1)
Button(root, text='消费者2', width=10, height=1,
       command=lambda: xiaofei(2)).grid(row=5, column=2)
Button(root, text='消费者3', width=10, height=1,
       command=lambda: xiaofei(3)).grid(row=5, column=3)
Button(root, text='消费者4', width=10, height=1,
       command=lambda: xiaofei(4)).grid(row=5, column=4)

mainloop()
