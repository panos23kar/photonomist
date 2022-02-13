"""
Hosts the code for the Exclude window

|
"""
# Workaround for having it working both locally and in github actions
# import sys
# from pathlib import Path
# src_dir = Path(__file__).parents[1]
# sys.path.insert(0, src_dir)

import tkinter as tk

import importlib

from GUI.languages import en
from GUI.widgets import create_label, create_canvas, create_frame, create_scrollbar, \
                    create_check_button, create_int_var, create_button

from app.main import open_export_folder

class Exclude:
    """
    Draws the Exclude window

    |
    """

    def __init__(self, main_window) -> None:
        """
        Initializes the Exclude window

        :param main_window: GUI main window
        :type main_window: tkinter.Tk
        |
        """
        self.__y_check_button_link = 57
        self.main_window = main_window

    def draw_exclude_window(self, photos_roots):
        """
        Draws the whole layout of the Exclude window

        |
        """
        self.__photo_roots = photos_roots
        self.__exclude_window()
        self.__draws_canvas()
        self.__draws_frame()
        self.__canvas_create_window()
        self.__draws_scrollbar()
        self.__draws_label()
        self.__draws_checkboxes()
        self.__draws_run_button()
        self.__resize_canvas()
        if self.main_window.language!='en':
            self.__change_language()

    def __exclude_window(self):
        """
        Toplevel and title for the Exclude window

        |
        """
        self.exclude_toplevel = tk.Toplevel(self.main_window)
        self.exclude_toplevel.title(en.EXCl_TITLE)
        # Gets the 'full' focus of the app
        self.exclude_toplevel.grab_set()

    def __draws_canvas(self):
        """
        Draws the canvas for the Exclude window
        Canvas, in combination with the frame, is needed for the scrollbar

        |
        """
        self.__exclude_canvas = create_canvas(self.exclude_toplevel)
        self.__exclude_canvas.bind_all("<MouseWheel>", self.__on_mousewheel)

    def __draws_frame(self):
        """
        Draws the frame which will be attached to canvas for the Exclude window
        Frame, in combination with the canvas, is needed for the scrollbar

        |
        """
        self.__exclude_frame = create_frame(self.__exclude_canvas, padx=40)
        self.__exclude_frame.bind("<Configure>", lambda event, canvas=self.__exclude_canvas: self.__on_frame_configure())

    def __on_mousewheel(self, event):
        """
        It listens for mouse's wheel scrolling
        Connected with a canvas widget

        https://stackoverflow.com/questions/17355902/tkinter-binding-mousewheel-to-scrollbar 

        :param event: Specifies x, y for mousewheel ex: MouseWheel event delta=-120 x=698 y=340
        :type event: tkinter.Event
        |
        """
        self.__exclude_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def __on_frame_configure(self):
        """
        Resets the scroll region to encompass the inner frame

        |
        """
        self.__exclude_canvas.configure(scrollregion=self.__exclude_canvas.bbox("all"))

    def __canvas_create_window(self):
        """
        It creates a canvas object, similar to a line, rectangle, image, etc. 
        Like a line or rectangle, this canvas object has attributes that define what it looks like.
        In the case of a window object, one of the attributes is window which specifies a widget to 
        be displayed as the object.

        If you add a frame in a canvas with pack, place, or grid it will appear inside the canvas but 
        it won't be part of the canvas. That means that if you attach scrollbars to the canvas, the 
        frame will not scroll. By using create_window, the frame becomes part of the canvas, and can 
        be manipulated and scrolled like any other canvas object.

        The value returned from calling create_window is an integer index which can be used later to refer to this object.

        https://stackoverflow.com/questions/58009398/tkinter-what-is-a-window-when-calling-tk-canvas-create-window

        |
        """
        self.__exclude_canvas.create_window((1,1), window=self.__exclude_frame, anchor="n")

    def __draws_scrollbar(self):
        """
        Draws the scrollbar for the Exclude window

        |
        """
        self.__exclude_scrollbar = create_scrollbar(self.exclude_toplevel, command=self.__exclude_canvas.yview)
        self.__exclude_canvas.configure(yscrollcommand=self.__exclude_scrollbar.set)
    
    def __calculate_number_photos(self):
        """
        Calculates the number of photos inside the photo_roots

        |
        """
        self.__number_of_photos = 0
        for photo_list in self.__photo_roots.values():
            self.__number_of_photos += len(photo_list)

    def __draws_label(self):
        """
        Draws the label/title for the Exclude window

        |
        """
        self.__calculate_number_photos()
        self.__exclude_number_photos_label = create_label(self.__exclude_frame, text=str(self.__number_of_photos) + en.EXCL_NUMBER_PHOTOS_LABEL, justify="center")
        self.__exclude_number_photos_label.pack(anchor="center")

    def __draws_checkboxes(self):
        """
        Draws the checkboxes to exclude photo folders from moving to other folder

        |
        """
        # Dictionary which will dynamically host a check button for every folder
        self.__check_buttons ={}
        # Dictionary which will dynamically host the int variable for every check button
        self.__check_button_variables ={}
        # Dictionary which will dynamically host the link(label) for each check button
        self.__check_button_links ={}

        self.__photos_folders = set(self.__photo_roots.keys())
        
        for photo_folder in self.__photos_folders:
            self.__create_check_button(photo_folder)
            self.__create_check_button_link(photo_folder)
            self.__y_check_button_link +=25

    def __create_check_button(self, photo_folder):
        """
        Creates an Int var together with a Checkbutton

        :param photo_folder: Path of the folder where the photos exist
        :type photo_folder: str
        |
        """
        self.__check_button_variables[photo_folder] = create_int_var(value=1)
        self.__check_buttons[photo_folder] = create_check_button(self.__exclude_frame, text=photo_folder, variable=self.__check_button_variables[photo_folder])
        self.__check_buttons[photo_folder].pack(anchor="w")

    def __create_check_button_link(self, photo_folder):
        """
        Creates the link close to checkbutton label for opening the corresponding folder

        :param photo_folder: Path of the folder where the photos exist
        :type photo_folder: str
        |
        """
        self.__check_button_links[photo_folder] = create_label(self.__exclude_frame, text=en.EXCL_LINK, font="Helvetica 8 bold", 
                                                               fg="blue", cursor="hand2", y=self.__y_check_button_link, x=self.__calculate_x_coord(len(photo_folder)))
        self.__check_button_links[photo_folder].bind("<Button-1>", lambda e, photo_folder=photo_folder:self.__open_folder(photo_folder))

    def __calculate_x_coord(self, num_of_chars):
        """
        Calculates the x "coordinate" of the link for each folder

        :param num_of_chars: Number of character that a path has
        :type num_of_chars: int
        |
        """
        l = [6.8, 6.8, 6.7, 6.25, 6.35, 6.2, 6.15, 6.2, 6.05, 6.05, 6, 5.9, 5.85]
        return int(num_of_chars*l[min(num_of_chars//10, 12)])

    def __open_folder(self, photo_folder):
        """
        Opens the corresponding photos folder

        :param photo_folder: Path of the folder where the photos exist
        :type photo_folder: str
        |
        """
        open_export_folder(photo_folder)
    
    def __resize_canvas(self):
        """
        Resizes the canvas in order the photo folders to fit nicely

        |
        """
        self.__exclude_frame.update()
        self.__exclude_canvas.configure(width=self.__exclude_frame.winfo_width())
        self.__exclude_canvas.configure(height=self.__exclude_frame.winfo_height())

    def __draws_run_button(self):
        """
        Draws the 'Good2Go' button

        |
        """
        self.__exclude_run_button = create_button(self.__exclude_frame, text=en.EXCL_RUN_BUTTON, command=self.__exclude_paths)
        self.__exclude_run_button.pack(side="bottom", padx=5, pady=5)

    def __exclude_paths(self):
        """
        Excludes the folders that the user has specifed from the tidying process

        |
        """
        for check_button in self.__check_buttons:
            if  self.__check_button_variables[check_button.replace('\\\\','\\')].get() == 0:
                if check_button in self.__photo_roots:
                    del self.__photo_roots[check_button]

        self.__close_toplevel()

    def __close_toplevel(self):
        """
        Closes the Exclude window

        |
        """
        self.main_window.exclude_window_state = 1
        self.exclude_toplevel.destroy()
        self.exclude_toplevel.update()

    def __change_language(self):
        """
        Changes the language

        |
        """
        language=importlib.import_module('languages.'+ self.main_window.language)

        self.exclude_toplevel.title(getattr(language, 'EXCl_TITLE'))

        self.__exclude_number_photos_label.config(text=str(self.__number_of_photos) + getattr(language, 'EXCL_NUMBER_PHOTOS_LABEL'))
        self.__exclude_run_button.config(text=getattr(language, 'EXCL_RUN_BUTTON'))
