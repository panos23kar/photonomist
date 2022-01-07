"""
Hosts the code for the loading window
"""
import tkinter as tk

from byte_stream import BYTESTREAM

from PIL import ImageTk, Image
from base64 import b64decode
from io import BytesIO


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