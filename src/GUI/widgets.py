"""
Provides widgets for all windows
"""
import tkinter as tk

def create_menu(master, tearoff=None):
    """
    Creates tkinter menu
    """
    return tk.Menu(master, tearoff=tearoff)