"""
Hosts the code for the main window
"""
import tkinter as tk
from tkinter import messagebox

from info import Info

from languages import en
from widgets import create_menu, create_label, create_string_variable, create_entry, create_button, create_frame, create_radio_button, create_check_button, create_int_var

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
        self.__find_photos_button()
        self.__export_path()
        self.__group_by_buttons()
        self.__folder_name_pattern()

    def __input_path(self):
        """
        Draws the input folder path widgets
        |
        """
        #Label
        self.__input_label = create_label(self.__gui, text=en.MAIN_INPUT_PATH, x=15, y=22)

        #String Variable
        self.__input_path_value = create_string_variable()

        #Entry
        self.__input_path_entry = create_entry(self.__gui, x=90, y=22, w=300, textvariable=self.__input_path_value)
        #TODO self.__check_input_entry

        #Button
        #TODO command
        self.__input_path_button = create_button(self.__gui, x=395, y=20, h=21, text=en.MAIN_PATH_BUTTON, command="TODO")

    def __find_photos_button(self):
        """
        Draws the find photos button
        |
        """
        #TODO command
        create_button(self.__gui, x=340, y=70, h=21, text=en.MAIN_FIND_PHOTOS_BUTTON, command="TODO")

    def __export_path(self):
        """
        Draws the export folder path widgets
        |
        """
        #Label
        self.__export_label = create_label(self.__gui, text=en.MAIN_EXPORT_PATH, x=10, y=140)

        #String Variable
        self.__export_path_value = create_string_variable()

        #Entry
        self.__export_path_entry = create_entry(self.__gui, x=90, y=142, w=300, textvariable=self.__export_path_value)

        #Button
        #TODO command
        self.__export_path_button = create_button(self.__gui, x=395, y=140, h=21, text=en.MAIN_PATH_BUTTON, command="TODO")

    def __group_by_buttons(self):
        """
        Draws the group by 'day', 'month', 'year' radio buttons
        |
        """
        #Frame
        self.__group_by_frame = create_frame(self.__gui, x=20, y=190, bd=2)
        
        #Label
        self.__group_by_label = create_label(self.__group_by_frame, text=en.MAIN_GROUP_BY_LABEL)
        self.__group_by_label.grid(row=0, column=0, columnspan=3, sticky="w", pady=5)

        #String Variable
        self.__group_by_string_variable = create_string_variable()

        #Day Radio Button
        self.__day_radio_button = create_radio_button(self.__group_by_frame, text=en.MAIN_DAY_RADIO_BUTTON, row=1, column=0, width=8,
                                                      variable=self.__group_by_string_variable, value=en.MAIN_DAY_RADIO_BUTTON_VALUE, indicatoron=0, bd=2)
        self.__group_by_string_variable.set(en.MAIN_DAY_RADIO_BUTTON_VALUE)

        #Month Radio Button
        self.__month_radio_button = create_radio_button(self.__group_by_frame, text=en.MAIN_MONTH_RADIO_BUTTON, row=1, column=1, width=8,
                                                      variable=self.__group_by_string_variable, value=en.MAIN_MONTH_RADIO_BUTTON_VALUE, indicatoron=0, bd=2)

        #Year Radio Button
        self.__year_radio_button = create_radio_button(self.__group_by_frame, text=en.MAIN_YEAR_RADIO_BUTTON, row=1, column=2, width=8,
                                                      variable=self.__group_by_string_variable, value=en.MAIN_YEAR_RADIO_BUTTON_VALUE, indicatoron=0, bd=2)

    def __folder_name_pattern(self):
        """
        Draws the checkboxes '_place', '_reason', '_people' which define a folder's name pattern
        |
        """
        #Label
        self.__name_pattern_label = create_label(self.__gui, text=en.MAIN_NAME_PATTERN_LABEL, x=20, y=270)

        #Place
        self.__place_int_variable = create_int_var()
        create_check_button(self.__gui, text=en.MAIN_NAME_PATTERN_PLACE, x=20, y=290, variable=self.__place_int_variable)

        #Reason
        self.__reason_int_variable = create_int_var()
        create_check_button(self.__gui, text=en.MAIN_NAME_PATTERN_REASON, x=20, y=310, variable=self.__reason_int_variable)

        #People
        self.__people_int_variable = create_int_var()
        create_check_button(self.__gui, text=en.MAIN_NAME_PATTERN_PEOPLE, x=20, y=330, variable=self.__people_int_variable)


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