"""
Hosts the code for the main window
"""
import tkinter as tk
from tkinter import messagebox

from info import Info

from languages import en
from widgets import create_menu, create_label, create_string_variable, create_entry, create_button

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
        self.__draw_main_window()
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
    
    def __draw_main_window(self):
        """
        Draws the whole layout of the main window
        |
        """
        self.__main_window()
        self.__input_path()

    def __input_path(self):
        """
        Draws the input folder path widgets
        |
        """
        #Label
        self.__input_label = create_label(self.__gui, text=en.MAIN_INPUT_PATH, x=20, y=22)

        #String Variable
        self.__input_path_value = create_string_variable()

        #Entry
        self.__input_path_entry = create_entry(self.__gui, x=90, y=22, w=300, textvariable=self.__input_path_value)
        #TODO self.__check_input_entry

        #Button
        #TODO command
        self.__input_path_button = create_button(self.__gui, x=395, y=20, h=21, text=en.MAIN_INPUT_PATH_BUTTON, command="TODO")

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

        ## SubMenu Info
        self.__main_menu.add_command(label=en.MAIN_MENU_INFO, command=Info(self.__gui).show_info_window, underline=1)

    def __quit(self):
        """
        Quits the applicaton
        |
        """
        if messagebox.askyesno("", en.QUIT_MESSAGE):
            self.__gui.destroy()

if __name__ == "__main__":
    Main()