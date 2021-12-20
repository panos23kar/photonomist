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
        self.__start_gui() 
    
    def __main_window(self):
        """
        Title and dimensions for the main window
        |
        """
        self.__gui.title(en.MAIN_TITLE)
        self.__gui.geometry("440x420")
    
    def __start_gui(self):
        """
        Starts the graphical user interface
        |
        """
        self.__gui.mainloop()