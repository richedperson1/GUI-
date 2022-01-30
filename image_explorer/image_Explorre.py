import logging as lg
from tkinter import *
from PIL import ImageTk, Image
import os

"""
Enter image path directory.
"""

path = 'F:\\pratices_new\\new_year_start\\I-Neuron\\GUI Python\\image explorer\\image\\'

root = Tk()
lg.basicConfig(filename='image_explorer.log', level=lg.INFO,
               format='%(levelname)s %(asctime)s %(message)s')


lst = os.listdir(path)
listing = []

"""

Resize image into 300*205 so that every image not affect windows size

"""
try:
    """

    This will automatically fetch image data from given directory and into the window 

    """

    for name in lst:
        listing.append(ImageTk.PhotoImage(Image.open(
            path+name).resize((300, 205), Image.ANTIALIAS)))

    image = listing[0]
    next_iter = 0

except Exception as e:
    lg.exception(str(e))
    lg.error(str(e))


def forward():
    """ 

    logging file are made to recheck wheather or not it's working ;

    To forward the image I used global variable hence forward and reverse can be possible

    """
    try:
        global img_label
        global next_iter
        img_label.grid_forget()

        if next_iter <= 3:
            next_iter += 1
        else:
            next_iter = 0

        img_label = Label(image=listing[next_iter])
        img_label.grid(row=0, column=0, columnspan=3)

    except Exception as e:
        lg.exception(str(e))
        lg.error(str(e))


def back():
    try:
        global next_iter
        global img_label
        img_label.grid_forget()
        next_iter -= 1
        next_iter = max(next_iter, 0)
        """
        I used 0 index image at most to reverse image after it's remain in 0 index
        
        """

        img_label = Label(image=listing[next_iter])
        img_label.grid(row=0, column=0, columnspan=3)
    except Exception as e:
        lg.exception(str(e))
        lg.error(str(e))


try:
    """
    This is used for error handling and to avoid crashing of program
    """
    img_label = Label(image=image)  # Showing First image in directory
    next = Button(root, text='>>', command=forward)
    back = Button(root, text='<<', command=back)
    exit_b = Button(root, text='Exit', command=root.quit)

    exit_b.grid(row=1, column=1)
    next.grid(row=1, column=2)
    back.grid(row=1, column=0)
    img_label.grid(row=0, column=0, columnspan=3)

except Exception as e:
    lg.error(str(e))
    lg.exception(str(e))


root.mainloop()

"""feel free to make change for improving it ...!"""
