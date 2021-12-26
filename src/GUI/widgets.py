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


def create_label(master, text, x, y, font="Helvetica 10", justify=None, fg=None, cursor=None):
    """
    Creates a Label widget
    |
    """
    label = tk.Label(master, text=text, font=font, justify=justify, fg=fg, cursor=cursor)
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