"""
Hosts the code for the Info window

|
"""

import tkinter as tk
import webbrowser

# from GUI.languages import en

# from GUI.widgets import create_label, create_text

from languages import en

from widgets import create_label, create_text

class Info:
    """
    Draws the Info window

    |
    """
    def __init__(self, main_window:object):
        """
        Initializes the Info window

        :param main_window: GUI main window
        :type main_window: tkinter.Tk
        |
        """
        self.__main_window = main_window

    def show_info_window(self):
        """
        Shows the Info window. Calls the different methods which compose the Info window

        |
        """
        self.__info_window()

        # Gets the 'full' focus of the app
        self.__info.grab_set()

        self.__title()
        self.__aim()
        self.__name()
        self.__github()

        self.__email()

    def __info_window(self):
        """
        Title and dimensions for the Info window

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
        'States' the aim of photonomist for the Info window

        |
        """
        self.__aim_label = create_label(self.__info, text=en.INFO_AIM, x=10, y=40, justify="left")

    def __name(self):
        """
        'States' how photonomist took its name in the Info window

        |
        """
        self.__name_title_label = create_label(self.__info, text=en.INFO_NAME_TITLE, x=10, y=170, font="Helvetica 10 bold")

        self.__name_label = create_label(self.__info, text=en.INFO_NAME, x=10, y=190, justify="left")
    
    def __github(self):
        """
        'Writes' the github link in the Info window

        |
        """
        self.__github_link_label = create_label(self.__info, text=en.INFO_GITHUB_LINK, x=10, y=339, font="Helvetica 10 bold", fg="blue", cursor="hand2")
        self.__github_link_label.bind("<Button-1>", lambda e: self.__open_url(en.INFO_GITHUB_URL))

        self.__github_text_label = create_label(self.__info, text=en.INFO_GITHUB_TEXT, x=75, y=340)

    def __open_url(self, url:str):
        """
        Opens a browser tab with the provided url

        :param url: url to open
        :type url: str
        |
        """
        webbrowser.open_new(url)

    def __email(self):
        """
        'States' the email info in the Info window

        |
        """
        self.__email_text = create_text(self.__info, text=en.INFO_EMAIL, insert_num=0.1, width=26, height=1, x=10, y=245)
        # Gets the background color of the info window and applies it on the text-widget background
        self.__email_text.configure(bg=self.__info.cget('bg'), relief="flat")

        self.__email_label = create_label(self.__info, text=en.INFO_EMAIL_GOALS, x=10, y=265, justify="left")
