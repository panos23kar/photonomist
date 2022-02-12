"""
Hosts the code for the Loading window

|
"""
import tkinter as tk

from GUI.byte_stream import BYTESTREAM
from GUI.languages import en
from GUI.widgets import create_canvas

# from byte_stream import BYTESTREAM
# from languages import en
# from widgets import create_canvas

from PIL import ImageTk, Image
from base64 import b64decode
from io import BytesIO

from threading import Thread


class Loading:
    """
    Draws the Loading window
    
    |
    """

    def __init__(self, main_window:object):
        """
        Initializes the Loading window

        :param main_window: GUI main window
        :type main_window: tkinter.Tk        
        |
        """
        self.main_window = main_window
        self.__angle = 0
        self.__load_image = Image.open(BytesIO(b64decode(BYTESTREAM)))

    def start_threads(self, func:callable):
        """
        Starts 2 threads:

          1) Shows the loading image
          2) Works on user's request

        :param func: function to run in a separate thread
        :type func: callable
        |
        """
        self.__load_func = Thread(target=func)
        self.__load_func.start()
        # Loading Image window while photonomist is working on user's request
        self.__load_draw_image()

    def __load_draw_image(self):
        """
        Draws the rotating image for as long as photonomist is working

        |
        """
        if not self.__load_func.is_alive():
            self.__close_toplevel()
        else:
            self.__loading_window()
            self.__draws_canvas()
            self.__update_load_w = self.__draw_loading_camera().__next__
            self.__loading_canvas.after(100, self.__update_load_w)

    def __close_toplevel(self):
        """
        Closes the Loading window

        |
        """
        self.__loading_toplevel.destroy()
        self.__loading_toplevel.update()

    def __loading_window(self):
        """
        Toplevel and title for the Loading window

        |
        """
        self.__loading_toplevel = tk.Toplevel(self.main_window)
        self.__loading_toplevel.title(en.LOAD_TITLE)
        self.__loading_toplevel.grab_set()

    def __draws_canvas(self):
        """
        Draws the canvas for the Loading window

        |
        """
        self.__loading_canvas = create_canvas(self.__loading_toplevel, width=500, height=500)

    def __draw_loading_camera(self):
        """
        Draws and rotates the loading image window while photonomist is working

        |
        """
        while self.__load_func.is_alive():
            self.__tkimage = ImageTk.PhotoImage(self.__load_image.rotate(self.__angle))
            self.__canvas_obj = self.__loading_canvas.create_image(250, 250, image=self.__tkimage)
            self.__loading_toplevel.after(30,self.__update_load_w)
            yield
            self.__loading_canvas.delete(self.__canvas_obj)
            self.__angle = (self.__angle-10)%360

        self.__close_toplevel()
