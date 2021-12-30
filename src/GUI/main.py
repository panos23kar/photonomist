"""
Hosts the code for the main window
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

from functools import partial

from info import Info
from exclude import Exclude

from languages import en
from widgets import create_menu, create_label, create_string_variable, \
                    create_entry, create_button, create_frame, create_radio_button, \
                    create_check_button, create_int_var, change_color

from src.main import input_path_validation


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
        self.__initiate_exclude_window()
        self.__draw_main_window()
        self.__menu()
        self.__start_gui() 
    
    def __start_gui(self):
        """
        Starts the graphical user interface
        |
        """
        self.__gui.mainloop()
    
    def __initiate_exclude_window(self):
        """
        Initiates the exclude window
        |
        """
        self.excl_w = Exclude(self.__gui)

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
        self.__run_button()

    def __main_window(self):
        """
        Title and dimensions for the main window
        |
        """
        self.__gui.title(en.MAIN_TITLE)
        self.__gui.geometry("440x420")

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

        #Constantly checks if the user has specified an input path
        self.__input_path_value.trace('w', self.__check_input_path)

        #Button
        self.__input_path_button = create_button(self.__gui, x=395, y=20, h=21, text=en.MAIN_PATH_BUTTON, command=partial(self.__file_explorer, 'input'))

        #Invalid path

        ##String Variable
        self.__input_path_invalid_value = create_string_variable()

        ##Label
        self.__input_path_invalid_label = create_label(self.__gui, textvariable=self.__input_path_invalid_value, fg="red")




    def __find_photos_button(self):
        """
        Draws the find photos button
        |
        """
        self.__find_photos_button = create_button(self.__gui, x=340, y=70, h=21, text=en.MAIN_FIND_PHOTOS_BUTTON, command=self.excl_w.draw_exclude_window)

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
        self.__export_path_button = create_button(self.__gui, x=395, y=140, h=21, text=en.MAIN_PATH_BUTTON, command=partial(self.__file_explorer, 'export'))

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
        self.__int_variable_place = create_int_var()
        self.__check_button_place = create_check_button(self.__gui, text=en.MAIN_NAME_PATTERN_PLACE, x=20, y=290, variable=self.__int_variable_place)

        #Reason
        self.__int_variable_reason = create_int_var()
        self.__check_button_reason = create_check_button(self.__gui, text=en.MAIN_NAME_PATTERN_REASON, x=20, y=310, variable=self.__int_variable_reason)

        #People
        self.__int_variable_people = create_int_var()
        self.__check_button_people = create_check_button(self.__gui, text=en.MAIN_NAME_PATTERN_PEOPLE, x=20, y=330, variable=self.__int_variable_people)

    def __run_button(self):
        """
        Draws the run application button
        |
        """
        #TODO command
        self.__run_button = create_button(self.__gui, x=310, y=380, h=21, text=en.MAIN_RUN_APP_BUTTON, command="TODO", state="disabled")

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

    def __file_explorer(self, mode):
        """
        Opens file dialog in order the user to open a folder path
        |
        """
        folder_path = filedialog.askdirectory(initialdir = "/",title=en.MAIN_FILE_EXPLORER_MESSAGE)
        
        if mode == 'input':
            self.__input_path_value.set(folder_path)
        
        if mode == 'export':
            self.__export_path_value.set(folder_path)
        
        #In case that a user has already specify a folder-path and clicks again the input folder path button
        if mode == 'input':
            self.__run_button["state"] = "disabled"
    
    def __check_input_path(self, *args):
        """
        Whenever the user specifies a new input path, it disables the run button and changes the color
        of the find photos button to indicate that the user has to click it!
        |
        """
        # *args is there to deal with the error --> TypeError: __check_input_path() takes 1 positional argument but 4 were given

        self.__run_button["state"] = "disabled"
        change_color(self.__find_photos_button,'lightpink')

    def __group_option(self):
        """
        Specifies if the photos will be ordered by day, year or month
        depending on user's option
        |
        """
        #TODO Use it later in run_app
        user_option = self.__group_by_string_variable.get()

        if user_option == 'month':
            return False, True
        elif user_option == 'year':
            return True, False
        else:
            return False, False

    def __create_name_pattern(self):
        """
        Constructs the name pattern to be user as folders' name
        |
        """
        #TODO Use it later in run_app
        #TODO Hardcoded --> store name_pattern variables in a dict and dynamically get their names
        name_pattern = ""
        for var_name in [(self.__int_variable_place, '_place'), 
                         (self.__int_variable_reason, '_reason'), 
                         (self.__int_variable_people, '_people')]:
            if var_name[0].get():
                name_pattern += var_name[1]
        return name_pattern

    def __validate_input_path(self):
        try:
            self.__photos_roots = input_path_validation(self.__widgets["input_path_value"].get())
        except Exception as e:
            self.__photos_roots = ""
            self.__widgets["input_invalid_path_value"].set(str(e))
            self.__input_invalid_path_value
        else:
            self.__widgets["input_invalid_path_value"].set("")


if __name__ == "__main__":
    Main()