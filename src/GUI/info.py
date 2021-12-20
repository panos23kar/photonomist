"""
Hosts the code for the info window
"""

import tkinter as tk
import webbrowser


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

        # Gets the 'full' focus of the app
        self.__info_window.grab_set()