"""
Hosts the code for the Main window

|
"""
# Workaround for having it working both locally and in github actions
import sys
from pathlib import Path
src_dir = Path(__file__).parents[1]
sys.path.insert(0, src_dir)

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

from functools import partial
import importlib

from GUI.info import Info
from GUI.exclude import Exclude
from GUI.loading import Loading

from GUI.languages import en
from GUI.widgets import create_menu, create_label, create_string_variable, \
                    create_entry, create_button, create_frame, create_radio_button, \
                    create_check_button, create_int_var, change_color

# from info import Info
# from exclude import Exclude
# from loading import Loading

# from languages import en
# from widgets import create_menu, create_label, create_string_variable, \
#                     create_entry, create_button, create_frame, create_radio_button, \
#                     create_check_button, create_int_var, change_color

from app.main import input_path_validation, export_path_validation, \
                         tidy_photos, open_export_folder

# from src.app.main import input_path_validation, export_path_validation, \
#                          tidy_photos, open_export_folder

class Main:
    """
    Draws the Main window of the graphical user interface (GUI)
    
    |
    """

    def __init__(self) -> None:
        """
        Initializes the Main window
        
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
        Initiates the Exclude window
        
        |
        """
        self.exclude_window = Exclude(self.__gui)

    def __draw_main_window(self):
        """
        Draws the layout of the Main window
        
        |
        """
        self.__main_window()
        self.__input_path()
        self.__draw_find_photos_button()
        self.__export_path()
        self.__group_by_buttons()
        self.__folder_name_pattern()
        self.__run_button()

    def __main_window(self):
        """
        Title, dimensions and languuage for the Main window
        
        |
        """
        self.__gui.title(en.MAIN_TITLE)
        self.__gui.geometry("440x420")
        self.__gui.language = 'en'

    def __input_path(self):
        """
        Draws the widgets for the 'input path'

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
        self.__input_path_invalid_label = create_label(self.__gui, text='',x=20, y=47, textvariable=self.__input_path_invalid_value, fg="red")

    def __draw_find_photos_button(self):
        """
        Draws the 'find photos' button

        |
        """
        self.__find_photos_button = create_button(self.__gui, x=340, y=70, h=21, text=en.MAIN_FIND_PHOTOS_BUTTON, command=self.__trigger_exclude_window)

    def __export_path(self):
        """
        Draws the widgets for the 'export folder'

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

        #Invalid path
        ##String Variable
        self.__export_path_invalid_value = create_string_variable()

        ##Label
        self.__export_path_invalid_label = create_label(self.__gui, text='',x=20, y=167, textvariable=self.__export_path_invalid_value, fg="red")

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
        self.__run_button = create_button(self.__gui, x=310, y=380, h=21, text=en.MAIN_RUN_APP_BUTTON, state="disabled", command=partial(Loading(self.__gui).start_threads, self.__run_app))

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

        #Languages
        self.__Lang_sub_menu = create_menu(self.__sub_menu_file, tearoff=0)
        self.__Lang_sub_menu.add_command(label='English', command=partial(self.__change_language, 'en'))
        self.__Lang_sub_menu.add_command(label='Eλληνικά', command=partial(self.__change_language, 'gr'))

        ##add the File menu to the menubar
        self.__sub_menu_file.add_cascade(label=en.MAIN_MENU_LANGUAGES,  menu=self.__Lang_sub_menu)

        # Separator
        self.__sub_menu_file.add_separator()
        self.__sub_menu_file.add_command(label=en.MAIN_MENU_QUIT, underline=0, command=self.__quit)

        ## SubMenu Info
        self.__main_menu.add_command(label=en.MAIN_MENU_INFO, command=Info(self.__gui).show_info_window, underline=1)

    def __change_language(self, lang:str):
        """
        Changes the language of the app

        :param lang: language specified by the user
        :type lang: str
        |
        """
        language=importlib.import_module('languages.'+lang)
        self.__gui.language = lang

        self.__gui.title(getattr(language, 'MAIN_TITLE'))

        self.__main_menu.entryconfig(1, label=getattr(language, 'MAIN_MENU_FILE'))
        self.__sub_menu_file.entryconfig(0, label=getattr(language, 'MAIN_MENU_LANGUAGES'))
        self.__sub_menu_file.entryconfig(4, label=getattr(language, 'MAIN_MENU_QUIT'))
        self.__main_menu.entryconfig(3, label=getattr(language, 'MAIN_MENU_INFO'))

        self.__input_label.config(text=getattr(language, 'MAIN_INPUT_PATH'))
        self.__find_photos_button.config(text=getattr(language, 'MAIN_FIND_PHOTOS_BUTTON'))
        self.__export_label.config(text=getattr(language, 'MAIN_EXPORT_PATH'))
        self.__day_radio_button.config(text=getattr(language, 'MAIN_DAY_RADIO_BUTTON'))
        self.__month_radio_button.config(text=getattr(language, 'MAIN_MONTH_RADIO_BUTTON'))
        self.__year_radio_button.config(text=getattr(language, 'MAIN_YEAR_RADIO_BUTTON'))
        self.__group_by_label.config(text=getattr(language, 'MAIN_GROUP_BY_LABEL'))
        self.__name_pattern_label.config(text=getattr(language, 'MAIN_NAME_PATTERN_LABEL'))
        self.__check_button_place.config(text=getattr(language, 'MAIN_NAME_PATTERN_PLACE'))
        self.__check_button_reason.config(text=getattr(language, 'MAIN_NAME_PATTERN_REASON'))
        self.__check_button_people.config(text=getattr(language, 'MAIN_NAME_PATTERN_PEOPLE'))
        self.__run_button.config(text=getattr(language, 'MAIN_RUN_APP_BUTTON'))

    def __quit(self):
        """
        Quits the applicaton

        |
        """
        if messagebox.askyesno("", en.QUIT_MESSAGE):
            self.__gui.destroy()

    def __file_explorer(self, mode:str):
        """
        Opens file dialog in order the user to open a folder path

        :param mode: could be 'input' or 'export'. Specifies if will open the file explorer for input or export path
        :type mode: str
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

    def __check_input_path(self, *args:any):
        """
        Whenever the user specifies a new input path, it disables the run button and changes the color
        of the find photos button to indicate that the user has to click it!

        :param *args: *args is there to deal with the error --> TypeError: __check_input_path() takes 1 positional argument but 4 were given
        :type *args: any
        |
        """
        # *args is there to deal with the error --> TypeError: __check_input_path() takes 1 positional argument but 4 were given

        self.__run_button["state"] = "disabled"
        change_color(self.__find_photos_button,'lightpink')

    def __group_option(self):
        """
        Specifies if the photos will be ordered by 'day', 'year' or 'month'

        :return: Returns a tupple which indicates if the photos will be ordered by day, month, year
        :rtype: tupple
        |
        """
        user_option = self.__group_by_string_variable.get()

        if user_option == 'month':
            return False, True
        elif user_option == 'year':
            return True, False
        else:
            return False, False

    def __create_name_pattern(self):
        """
        Constructs the name pattern to be used as folders' name

        :return: The pattern that will be used as name for the folders
        :rtype: str
        |
        """
        language=importlib.import_module('languages.' + self.__gui.language)
        name_pattern = ""
        for var_name in [(self.__int_variable_place, getattr(language, 'MAIN_NAME_PATTERN_PLACE')), 
                         (self.__int_variable_reason, getattr(language, 'MAIN_NAME_PATTERN_REASON')), 
                         (self.__int_variable_people, getattr(language, 'MAIN_NAME_PATTERN_PEOPLE'))]:
            if var_name[0].get():
                name_pattern += var_name[1]
        return name_pattern

    def __trigger_exclude_window(self):
        """
        Checks if the input path is valid and contains photos via 
        validate_input_path
        Then triggers Exclude window

        |
        """
        self.photos_roots = {}
        self.__validate_input_path()

        if self.photos_roots:
            self.exclude_window.draw_exclude_window(self.photos_roots)

        self.__gui.wait_window(self.exclude_window.exclude_toplevel)

        if self.__gui.exclude_window_state==1:
            self.__run_button["state"] = "normal"
            change_color(self.__find_photos_button,'grey95')

    def __validate_input_path(self):
        """
        Checks if the provided input path is valid and contains photos
        If not, it shows an error message

        |
        """
        self.__gui.exclude_window_state = 0
        try:
            self.photos_roots = input_path_validation(self.__input_path_value.get())
        except Exception as e:
            if self.__gui.language != 'en':
                self.__input_path_invalid_value.set(self.__show_error_message(str(e)))
            else:
                self.__input_path_invalid_value.set(str(e))
        else:
            self.__input_path_invalid_value.set("")

    def __validate_export_path(self):
        """
        Checks if the provided export path is valid and there is enough memory for the photos
        If not, it shows an error message

        |
        """
        try:
            export_path_validation(self.__export_path_value.get(), self.__input_path_value.get(), self.photos_roots)
        except Exception as e:
            if self.__gui.language != 'en':
                self.__export_path_invalid_value.set(self.__show_error_message(str(e)))
            else:
                self.__export_path_invalid_value.set(str(e))
        else:
            self.__export_path_invalid_value.set("")

    def __show_error_message(self, error_message):
        """
        Returns the translated error message

        :return: Error message to be shown
        :rtype: str
        |
        """
        language=importlib.import_module('languages.'+ self.__gui.language)

        if "Your input is not a valid path!" == error_message or "The provided path was not found!" == error_message:
            return getattr(language, 'NOT_VALID_PATH')
        elif "The provided path does not contain any files!" == error_message:
            return getattr(language, 'NO_FILES_IN_PATH')
        elif "The provided path does not contain any .jpg, .jpeg, .nef or .cr2 files" == error_message:
            return getattr(language, 'NO_PHOTOS_IN_PATH')
        elif error_message.startswith("You need at least"):
            return getattr(language, 'NOT_ENOUGH_SPACE')

    def __run_app(self):
        """
        Gets the photo_roots dict from Exclude window without the excluded folders
        Activates the run button

        |
        """
        self.__validate_input_path()
        self.__validate_export_path()

        year, month = self.__group_option()
        name_pattern = self.__create_name_pattern()

        #tidy_photos(self.__export_path_value.get(), self.photos_roots, year=year, month=month, name_pattern=name_pattern)
        open_export_folder(self.__export_path_value.get())


if __name__ == "__main__":
    Main()
