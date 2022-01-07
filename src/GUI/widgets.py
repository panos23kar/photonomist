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


def create_label(master, text, x=0, y=0, font="Helvetica 10",textvariable=None, justify=None, fg=None, cursor=None):
    """
    Creates a Label widget
    |
    """
    label = tk.Label(master, text=text, font=font, justify=justify, fg=fg, cursor=cursor, textvariable=textvariable)
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


def create_button(master, text, command, x=0, y=0, h=0, state='active'):
    """
    Creates a Button widget
    |
    """
    button = tk.Button(master, text=text, command = command, state=state)
    if x and y and h:
        button.place(x=x, y=y, height=h)
    return button


def create_frame(master, x=0, y=0, bd=0, background="grey95", padx=0):
    """
    Creates a Frame widget
    |
    """
    frame = tk.Frame(master, bd=bd, background=background, padx=padx)
    if x and y:
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

def create_check_button(master, text, variable, x=0, y=0, onvalue = 1,  offvalue = 0):
    """
    Create a Check Button widget
    |
    """
    check_button = tk.Checkbutton(master, text=text, variable=variable, onvalue=onvalue, offvalue=offvalue)
    if x and y:
        check_button.place(x=x, y=y)
    return check_button

def create_int_var(value=0):
    """
    Create an Int variable widget
    |
    """
    return tk.IntVar(value=value)


def change_color(widget, color):
    """
    Gets a widget and changes its background color
    |
    """
    widget.config(background=color)


def create_canvas(master, borderwidth=0, side='left', fill='both', expand=True):
    """
    Create a Canvas widget
    |
    """
    canvas = tk.Canvas(master, borderwidth=borderwidth)
    canvas.pack(side=side, fill=fill, expand=expand)
    return canvas


def create_scrollbar(master, command, orient='vertical', side='right', fill='y'):
    """
    Create a scrollbar widget
    |
    """
    scrollbar = tk.Scrollbar(master, orient=orient, command=command)
    scrollbar.pack(side=side, fill=fill)
    return scrollbar
