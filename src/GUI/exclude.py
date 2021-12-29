"""
Hosts the code for the exclude window
"""
import tkinter as tk

from languages import en

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

    def __exclude_window(self):
        """
        Title and dimensions for the exclude window
        |
        """
        self.__exclude = tk.Toplevel(self.__main_window)
        self.__exclude.title(en.EXCl_TITLE)
        # Gets the 'full' focus of the app
        self.__exclude.grab_set()
