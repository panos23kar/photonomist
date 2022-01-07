"""
Hosts the code for the loading window
"""
import tkinter as tk

from byte_stream import BYTESTREAM

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