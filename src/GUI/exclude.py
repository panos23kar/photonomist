"""
Hosts the code for the exclude window
"""
import tkinter as tk

from languages import en

from widgets import create_canvas, create_frame

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
        self.____exclude_frame = create_frame(self.__exclude_canvas)
        self.____exclude_frame.bind("<Configure>", lambda event, canvas=self.__exclude_canvas: self.__on_frame_configure())
    
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