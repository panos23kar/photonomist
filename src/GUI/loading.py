"""
Hosts the code for the loading window
"""
import tkinter as tk

from PIL import ImageTk, Image
from base64 import b64decode
from io import BytesIO
import json


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