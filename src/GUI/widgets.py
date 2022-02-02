"""
Provides widgets for all GUI windows

|
"""
import tkinter as tk


def create_menu(master:object, tearoff:int=None):
    """
    Creates tkinter menu

    :param master: tkinter instance
    :type master: tkinter.Tk
    :param tearoff: tearoff allows you to detach menus for the main window creating floating menus
    :type tearoff: int
    :return: Instance of tk.Menu
    :rtype: tk.Menu
    |
    """
    return tk.Menu(master, tearoff=tearoff)


def create_label(master:object, text:str, x:int=0, y:int=0, font:str="Helvetica 10",textvariable:object=None, justify:str=None, fg:str=None, cursor:str=None):
    """
    Creates a Label widget

    :param master: tkinter instance
    :type master: tkinter.Tk
    :param text: text for the label
    :type text: str
    :param x: Dimension on x-axis
    :type x: int
    :param y: Dimension on y-axis
    :type y: int
    :param font: font for the text of the label
    :type font: str
    :param textvariable: instance of tk.StringVar
    :type textvariable: tk.StringVar
    :param justify: defines where the text of the label will be 'positioned'
    :type justify: str
    :param fg: stands for foreground. Defines the color of the text 
    :type fg: str
    :param cursor: defines the cursor that will be used when hover over this label
    :type cursor: str
    :return: Instance of tk.Label
    :rtype: tk.Label
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


def create_canvas(master, borderwidth=0, side='left', fill='both', expand=True, width=None, height=None):
    """
    Create a Canvas widget
    
    |
    """
    if width and height:
        canvas = tk.Canvas(master, width=width, height=height, borderwidth=borderwidth)
    else:
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
