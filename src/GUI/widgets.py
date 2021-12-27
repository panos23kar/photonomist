"""
Provides widgets for all windows
"""
import tkinter as tk

def create_menu(master, tearoff=None):
    """
    Creates tkinter menu
    |
    """
    return tk.Menu(master, tearoff=tearoff)


def create_label(master, text, x=0, y=0, font="Helvetica 10", justify=None, fg=None, cursor=None):
    """
    Creates a Label widget
    |
    """
    label = tk.Label(master, text=text, font=font, justify=justify, fg=fg, cursor=cursor)
    if x and y:
        label.place(x=x, y=y)
    return label


def create_text(master, text, insert_num, width, height, x, y, font="Helvetica 10 bold"):
    """
    Creates a Text widget
    |
    """
    txt = tk.Text(master, width=width, height=height, font=font)
    txt.insert(insert_num, text)
    txt.place(x=x,y=y)
    return txt


def create_string_variable():
    """
    Creates a string variable which dynamically changes the value of the Entry widget
    |
    """
    return tk.StringVar()


def create_entry(master, x, y, w, textvariable):
    """
    Creates an Entry widget
    |
    """
    entry = tk.Entry(master, textvariable=textvariable)
    entry.place(x=x,y=y,width=w)
    return entry


def create_button(master, x, y, h, text, command, state='enabled'):
    """
    Creates a Button widget
    |
    """
    button = tk.Button(master, text=text, command = command, state=state)
    button.place(x=x, y=y, height=h)
    return button

def create_frame(master, x, y, bd=0):
    """
    Creates a Frame widget
    |
    """
    frame = tk.Frame(master, bd=2)
    frame.place(x=x, y=y)
    return frame

def create_radio_button(master, text, row, column, width, variable, value, indicatoron=None, bd=None):
    """
    Create a Radio Button widget
    |
    """
    radio_button = tk.Radiobutton(master, text=text, variable=variable)
    radio_button.config(indicatoron=indicatoron, bd=bd, width=width, value=value)
    radio_button.grid(row=row, column=column)
    return radio_button

def create_check_button(master, text, x, y, variable):
    """
    Create a Check Button widget
    |
    """
    check_button = tk.Checkbutton(master, text=text, variable=variable)
    check_button.place(x=x, y=y)
    return check_button

def create_int_var():
    """
    Create a Int variable widget
    |
    """
    return tk.IntVar()
