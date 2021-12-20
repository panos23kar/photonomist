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
    def __init__(self, main_window):
        """
        Initializes the info window
        |
        """
        self.__gui = main_window