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
        self.__aim()
        self.__name()
        self.__github()

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
    
    def __aim(self):
        """
        Draws the aim for the Info window
        |
        """
        self.__aim_label = create_label(self.__info, text=en.INFO_AIM, x=10, y=40, justify="left")
    
    def __name(self):
        """
        Draws the how photonomist took its name in the Info window
        |
        """
        self.__name_title_label = create_label(self.__info, text=en.INFO_NAME_TITLE, x=10, y=170, font="Helvetica 10 bold")

        self.__name_label = create_label(self.__info, text=en.INFO_NAME, x=10, y=190, justify="left")
    
    def __github(self):
        """
        Draws the github link in the Info window
        |
        """
        self.__github_link_label = create_label(self.__info, text=en.INFO_GITHUB_LINK, x=10, y=339, font="Helvetica 10 bold", fg="blue", cursor="hand2")
        self.__github_link_label.bind("<Button-1>", lambda e: self.__open_url(en.INFO_GITHUB_URL))

        self.__github_text_label = create_label(self.__info, text=en.INFO_GITHUB_TEXT, x=75, y=340)
    
    def __open_url(self, url):
        webbrowser.open_new(url)
