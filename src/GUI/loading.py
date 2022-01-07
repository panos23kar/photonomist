"""
Hosts the code for the loading window
"""
import tkinter as tk

from byte_stream import BYTESTREAM
from languages import en

from PIL import ImageTk, Image
from base64 import b64decode
from io import BytesIO

from threading import Thread


class Loading:
    """
    Draws the Loading window
    |
    """

    def __init__(self, main_window) -> None:
        """
        Initializes the loading window
        |
        """
        self.main_window = main_window
        self.__angle = 0
        self.__load_image = Image.open(BytesIO(b64decode(BYTESTREAM)))
    
    def start_threads(self, func):
        """
        Starts 2 threads:
          1) Shows the loading image
          2) Works on user's request
        |
        """
        self.__load_func = Thread(target=func)
        self.__load_func.start()
        # Loading Image window while photonomist is working on user's request
        self.__load_draw_image()
    
    def __load_draw_image(self):
        """
        Draws rotating image for as long as photonomist is working
        |
        """
        if not self.__load_func.is_alive():
            self.__close_toplevel()
        else:
            self.__loading_window()
            self.__update_load_w = self.__draw_loading_camera().__next__
            self.__load_w_canvas.after(100, self.__update_load_w)

    def __close_toplevel(self):
        """
        Closes the loading window
        |
        """
        self.__loading_toplevel.destroy()
        self.__loading_toplevel.update()

    def __loading_window(self):
        """
        Toplevel and title for the loading window
        |
        """
        self.__loading_toplevel = tk.Toplevel(self.__gui)
        self.__loading_toplevel.title(en.LOAD_TITLE)
        self.__loading_toplevel.grab_set()
