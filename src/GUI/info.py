"""
Hosts the code for the info window
"""

import tkinter as tk
import webbrowser

from languages import en

from widgets import create_label


class Info():
    """
    Draws the Info window
    |
    """
    def __init__(self, main):
        """
        Initializes the info window
        |
        """
        self.__main_window = main
    
    def show_info_window(self):
        """
        Shows the info window
        |
        """
        self.__info_window()

        # Gets the 'full' focus of the app
        self.__info.grab_set()

        self.__title()

    def __info_window(self):
        """
        Title and dimensions for the info window
        |
        """
        self.__info = tk.Toplevel(self.__main_window)
        self.__info.title(en.INFO_WINDOW_TITLE)
        self.__info.geometry("640x400")
    
    def __title(self):
        """
        Draws the title for the Info window
        |
        """
        self.__title_label = create_label(self.__info, text=en.INFO_TITLE, x=10, y=10, font="Helvetica 16 bold italic")