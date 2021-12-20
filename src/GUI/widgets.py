"""
Provides widgets for all windows
"""
import tkinter as tk

def create_menu(master, tearoff=None):
    """
    Creates tkinter menu
    """
    
    if tearoff:
        return tk.Menu(master, tearoff=tearoff)
    
    return tk.Menu(master)