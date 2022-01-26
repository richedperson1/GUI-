from tkinter import *

global add1
add1 = -1
root = Tk()

enty = Entry(root, width=35, borderwidth=5)
enty.grid(row=0, column=0, columnspan=4)


def button_add(number):
    try:
        current = enty.get()
        enty.delete(0, END)
        enty.insert(0, str(current)+str(number))
    except Exception as e:
        return e


def clear_button():
    enty.delete(0, END)


def addtion():
    try:
        global add1
        add1 = 1
        global first_num
        first_num = int(enty.get())
        enty.delete(0, END)
    except Exception as e:
        print(e)


def multi():
    try:
        global add1
        add1 = 2
        global first_num
        first_num = int(enty.get())
        enty.delete(0, END)
    except Exception as e:
        print(e)


def subtraction():
    try:
        global add1
        add1 = 3
        global first_num
        first_num = int(enty.get())
        enty.delete(0, END)
    except Exception as e:
        print(e)


def equal_to(add1):
    try:
        second = enty.get()
        enty.delete(0, END)
        if add1 == 1:
            sumi = int(first_num)+int(second)
            enty.insert(0, str(sumi))
        elif add1 == 2:
            sumi = int(first_num)*int(second)
            enty.insert(0, str(sumi))
        elif add1 == 3:
            sumi = int(first_num)-int(second)
            enty.insert(0, str(sumi))

        else:
            enty.insert(0, "Error")
    except Exception as e:
        print(e)


button_1 = Button(root, text='1', padx=40, pady=20,
                  command=lambda: button_add(1))
button_2 = Button(root, text='2', padx=40, pady=20,
                  command=lambda: button_add(2))
button_3 = Button(root, text='3', padx=40, pady=20,
                  command=lambda: button_add(3))
button_4 = Button(root, text='4', padx=40, pady=20,
                  command=lambda: button_add(4))
button_5 = Button(root, text='5', padx=40, pady=20,
                  command=lambda: button_add(5))
button_6 = Button(root, text='6', padx=40, pady=20,
                  command=lambda: button_add(6))
button_7 = Button(root, text='7', padx=40, pady=20,
                  command=lambda: button_add(7))
button_8 = Button(root, text='8', padx=40, pady=20,
                  command=lambda: button_add(8))
button_9 = Button(root, text='9', padx=40, pady=20,
                  command=lambda: button_add(9))
button_0 = Button(root, text='0', padx=40, pady=20,
                  command=lambda: button_add(0))


button_subtraction = Button(root, text="-", padx=40, pady=20,
                            command=subtraction)

button_multi = Button(root, text="*", padx=40, pady=20,
                      command=multi)

button_additon = Button(root, text="+", padx=40, pady=20,
                        command=addtion)
button_equal_t = Button(root, text="=", padx=40, pady=20,
                        command=lambda: equal_to(add1))
button_clear = Button(root, text="clear", padx=30, pady=20,
                      command=clear_button)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_multi.grid(row=5, column=1)
button_additon.grid(row=4, column=1)
button_subtraction.grid(row=5, column=2)
button_equal_t.grid(row=4, column=2, columnspan=2)


button_clear.grid(row=5, column=0)
root.mainloop()