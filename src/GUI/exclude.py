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
        Draws the canvas for the exclude window.
        Canvas (in combination with the frame) is needed for the scrollbar.
        |
        """
        self.__exclude_canvas = create_canvas(self.__exclude)
