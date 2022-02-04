"""
Provides widgets for all GUI windows

|
"""
import tkinter as tk
from xmlrpc.client import boolean


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


def create_text(master:object, text:str, insert_num:float, width:int, height:int, x:int, y:int, font:str="Helvetica 10 bold"):
    """
    Creates a Text widget

    :param master: tkinter instance
    :type master: tkinter.Tk
    :param text: text for the Text widget
    :type text: str
    :param insert_num: index location which specifies where the string will be placed 
    :type insert_num: float
    :param width: The width of the widget in characters (not pixels!), measured according to the current font size
    :type width: int
    :param height: The height of the widget in characters (not pixels!), measured according to the current font size
    :type height: int
    :param x: Dimension on x-axis
    :type x: int
    :param y: Dimension on y-axis
    :type y: int
    :param font: font for the text of the label
    :type font: str
    :return: Instance of tk.Text
    :rtype: tk.Text
    |
    """
    txt = tk.Text(master, width=width, height=height, font=font)
    txt.insert(insert_num, text)
    txt.place(x=x,y=y)
    return txt


def create_string_variable():
    """
    Creates a string variable which dynamically changes the value of the Entry widget
    
    :return: Instance of tk.StringVar
    :rtype: tk.StringVar
    |
    """
    return tk.StringVar()


def create_entry(master:object, x:int, y:int, w:int, textvariable:object):
    """
    Creates an Entry widget
    
    :param master: tkinter instance
    :type master: tkinter.Tk
    :param x: Dimension on x-axis
    :type x: int
    :param y: Dimension on y-axis
    :type y: int
    :param w: The width of the widget
    :type w: int
    :param textvariable: tk.StringVar variable
    :type textvariable: tk.StringVar
    :return: Instance of tk.Entry
    :rtype: tk.Entry
    |
    """
    entry = tk.Entry(master, textvariable=textvariable)
    entry.place(x=x,y=y,width=w)
    return entry


def create_button(master:object, text:str, command:callable, x:int=0, y:int=0, h:int=0, state:str='active'):
    """
    Creates a Button widget
    
    :param master: tkinter instance
    :type master: tkinter.Tk
    :param text: text for the Button widget
    :type text: str
    :param command: the function to be executed by this button 
    :type command: callable
    :param x: Dimension on x-axis
    :type x: int
    :param y: Dimension on y-axis
    :type y: int
    :param h: The height of the widget
    :type h: int
    :param state: defines if the button will be 'clickable' or not
    :type state: str
    :return: Instance of tk.Button
    :rtype: tk.Button
    |
    """
    button = tk.Button(master, text=text, command = command, state=state)
    if x and y and h:
        button.place(x=x, y=y, height=h)
    return button


def create_frame(master:object, x:int=0, y:int=0, bd:int=0, background:str="grey95", padx:int=0):
    """
    Creates a Frame widget
    
    :param master: tkinter instance
    :type master: tkinter.Tk
    :param x: Dimension on x-axis
    :type x: int
    :param y: Dimension on y-axis
    :type y: int
    :param bd: defines the border of the frame
    :type bd: int
    :param background: defines the color of the background
    :type background: str
    :param padx: Normally, a Frame fits tightly around its contents. To add N pixels of horizontal space inside the frame, set padx=N
    :type padx: int
    :return: Instance of tk.Frame
    :rtype: tk.Frame
    |
    """
    frame = tk.Frame(master, bd=bd, background=background, padx=padx)
    if x and y:
        frame.place(x=x, y=y)
    return frame


def create_radio_button(master:object, text:str, row:int, column:int, width:int, variable:object, value:str, indicatoron:int=None, bd:int=None):
    """
    Create a Radio Button widget

    :param master: tkinter instance
    :type master: tkinter.Tk
    :param text: text for the Radio Button widget
    :type text: str
    :param row: defines the row of the grid
    :type row: int
    :param column: defines the column of the grid
    :type column: int
    :param width: width of the radio button
    :type width: int
    :param variable: tk.StringVar variable
    :type variable: tk.StringVar
    :param value: defines the value that its related with the radio button
    :type value: str
    :param indicatoron: Instead of having radio buttons with circular holes containing white space, we can have radio buttons with the complete text in a box. We can do this by setting the indicatoron (stands for "indicator on") option to 0, which means that there will be no separate radio button indicator. The default is 1.
    :type indicatoron: int
    :param bd: defines the border of the frame
    :type bd: int
    :return: Instance of tk.Radiobutton
    :rtype: tk.Radiobutton
    |
    """
    radio_button = tk.Radiobutton(master, text=text, variable=variable)
    radio_button.config(indicatoron=indicatoron, bd=bd, width=width, value=value)
    radio_button.grid(row=row, column=column)
    return radio_button

def create_check_button(master:object, text:str, variable:object, x:int=0, y:int=0, onvalue:int=1,  offvalue:int=0):
    """
    Create a Check Button widget

    :param master: tkinter instance
    :type master: tkinter.Tk
    :param text: text for the Check Button widget
    :type text: str
    :param variable: tk.IntVar variable. Indicates if the checkbox is clicked
    :type variable: tk.IntVar
    :param onvalue: Normally, a checkbutton's associated control variable will be set to 1 when it is set (on). You can supply an alternate value for the on state by setting onvalue to that value.
    :type onvalue: int
    :param offvalue: Normally, a checkbutton's associated control variable will be set to 0 when it is cleared (off). You can supply an alternate value for the off state by setting offvalue to that value.
    :type offvalue: int
    :return: Instance of tk.Checkbutton
    :rtype: tk.Checkbutton
    |
    """
    check_button = tk.Checkbutton(master, text=text, variable=variable, onvalue=onvalue, offvalue=offvalue)
    if x and y:
        check_button.place(x=x, y=y)
    return check_button

def create_int_var(value:int=0):
    """
    Create an Int variable widget
    
    :param value: The initial value given to the integervariable. Defaults to 0
    :type value: int
    :return: Instance of tk.IntVar
    :rtype: tk.Intvar
    |
    """
    return tk.IntVar(value=value)


def change_color(widget:object, color:str):
    """
    Gets a widget and changes its background color
    
    :param widget: Tkinter wigdet 
    :type widget: tk object
    :param value: The color that will be used for the widget
    :type value: str
    |
    """
    widget.config(background=color)


def create_canvas(master:object, borderwidth:int=0, side:str='left', fill:str='both', expand:bool=True, width:int=None, height:int=None):
    """
    Create a Canvas widget
    
    :param master: tkinter instance
    :type master: tkinter.Tk
    :param borderwidth: width of the border
    :type borderwidth: int
    :param side: Determines which side of the canvas' parent packs against
    :type side: str
    :param fill: Determines whether canvas fills any extra space allocated to it by the packer, or keeps its own minimal dimensions
    :type fill: str
    :param expand: When set to true, canvas expands to fill any space not otherwise used in canvas' parent.
    :type expand: bool
    :param width: The width of the widget 
    :type width: int
    :param height: The height of the widget
    :type height: int
    :return: Instance of tk.Canvas
    :rtype: tk.Canvas
    |
    """
    if width and height:
        canvas = tk.Canvas(master, width=width, height=height, borderwidth=borderwidth)
    else:
        canvas = tk.Canvas(master, borderwidth=borderwidth)
    canvas.pack(side=side, fill=fill, expand=expand)
    return canvas


def create_scrollbar(master:object, command:object, orient:str='vertical', side:str='right', fill:str='y'):
    """
    Create a scrollbar widget
    
    :param master: tkinter instance
    :type master: tkinter.Tk
    :param command: the function which determines the scrollign of the scrollbar 
    :type command: callable
    :param orient: Set orient=HORIZONTAL for a horizontal scrollbar, orient=VERTICAL for a vertical one
    :type orient: str
    :param side: Determines which side of the scrollbar' parent packs against
    :type side: str
    :param fill: Determines which side the scrollbar will fill
    :type fill: str
    :return: Instance of tk.Scrollbar
    :rtype: tk.Scrollbar
    |
    """
    scrollbar = tk.Scrollbar(master, orient=orient, command=command)
    scrollbar.pack(side=side, fill=fill)
    return scrollbar
