"""
Hosts the code for the loading window
"""

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