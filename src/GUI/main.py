"""
Hosts the code for the main window
"""
import tkinter as tk
from tkinter import messagebox

from languages import en
from widgets import create_menu

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
        self.__menu()
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
    
    def __quit(self):
        """
        Quits the applicaton
        |
        """
        if messagebox.askyesno("", en.QUIT_MESSAGE):
            self.__gui.destroy()
    
    def __menu(self):
        """
        Menu on top of the window
        |
        """
        #  Main menu
        self.__main_menu = create_menu(self.__gui)
        self.__gui.config(menu=self.__main_menu)

        #  SubMenu
        ## SubMenu File
        self.__sub_menu_file = create_menu(self.__main_menu, tearoff=0)
        self.__main_menu.add_cascade(label=en.MAIN_MENU_FILE, menu=self.__sub_menu_file, underline=0)

        # Separator
        self.__sub_menu_file.add_separator()
        self.__sub_menu_file.add_command(label=en.MAIN_MENU_QUIT, underline=0, command=self.__quit)

        #SubMenu Info
        #TODO Connect it with info_window
        #self.__main_menu.add_command(label=en.MAIN_MENU_INFO, command=InfoWindow(self.__gui).info_app, underline=1)


if __name__ == "__main__":
    Main()