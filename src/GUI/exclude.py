"""
Hosts the code for the exclude window
"""
import tkinter as tk

from languages import en

from widgets import create_canvas, create_frame, create_scrollbar

class Exclude:
    """
    Draws the Exclude window
    |
    """

    def __init__(self, main_window) -> None:
        """
        Initializes the exclude window
        |
        """
        self.__main_window = main_window

    def draw_exclude_window(self):
        """
        Draws the whole layout of the exclude window
        |
        """
        self.__exclude_window()
        self.__draws_canvas()
        self.__draws_frame()
        self.__canvas_create_window()
        self.__draws_scrollbar()

    def __exclude_window(self):
        """
        Title and dimensions for the exclude window
        |
        """
        self.__exclude = tk.Toplevel(self.__main_window)
        self.__exclude.title(en.EXCl_TITLE)
        # Gets the 'full' focus of the app
        self.__exclude.grab_set()

    def __draws_canvas(self):
        """
        Draws the canvas for the exclude window
        Canvas, in combination with the frame, is needed for the scrollbar
        |
        """
        self.__exclude_canvas = create_canvas(self.__exclude)
        self.__exclude_canvas.bind_all("<MouseWheel>", self.__on_mousewheel)

    def __draws_frame(self):
        """
        Draws the frame for the which will be attached to canvas for the exclude window
        Frame, in combination with the canvas, is needed for the scrollbar
        |
        """
        self.__exclude_frame = create_frame(self.__exclude_canvas, padx=40)
        self.__exclude_frame.bind("<Configure>", lambda event, canvas=self.__exclude_canvas: self.__on_frame_configure())

    def __on_mousewheel(self, event):
        """
        It listens for mouse's wheel scrolling. 
        Connected with a canvas widget.

        https://stackoverflow.com/questions/17355902/tkinter-binding-mousewheel-to-scrollbar 
        |
        """
        self.__exclude_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def __on_frame_configure(self):
        """
        Resets the scroll region to encompass the inner frame
        |
        """
        self.__exclude_canvas.configure(scrollregion=self.__exclude_canvas.bbox("all"))

    def __canvas_create_window(self):
        """
        It creates a canvas object, similar to a line, rectangle, image, etc. 
        Like a line or rectangle, this canvas object has attributes that define what it looks like. 
        In the case of a window object, one of the attributes is window which specifies a widget to 
        be displayed as the object.

        If you add a frame in a canvas with pack, place, or grid it will appear inside the canvas but 
        it won't be part of the canvas. That means that if you attach scrollbars to the canvas, the 
        frame will not scroll. By using create_window, the frame becomes part of the canvas, and can 
        be manipulated and scrolled like any other canvas object.

        The value returned from calling create_window is an integer index which can be used later to refer to this object.

        https://stackoverflow.com/questions/58009398/tkinter-what-is-a-window-when-calling-tk-canvas-create-window
        |
        """
        self.__exclude_canvas.create_window((1,1), window=self.__exclude_frame, anchor="n")

    def __draws_scrollbar(self):
        """
        Draws the scrollbar for the exclude window
        |
        """
        self.__exclude_scrollbar = create_scrollbar(self.__exclude, command=self.__exclude_canvas.yview)