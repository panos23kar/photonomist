"""
Hosts the code for the main window
"""
import tkinter as tk

from languages import en

class Main:
    """
    Draws the main window of the graphical user interface (GUI)
    |
    """

    def __init__(self) -> None:
        """
        Initializes the main window
        |
        """
        self.__gui = tk.Tk()
        self.__main_window()
    
    def __main_window(self):
        """
        Title and dimensions for the main window
        |
        """
        self.__gui.title("Photonomist")
        self.__gui.geometry("440x420")