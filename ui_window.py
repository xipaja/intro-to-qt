import random
import sys
import logging

from PySide2 import QtWidgets, QtGui


'''
Interface that changes button color on press
'''

_log = logging.getLogger(__name__)
_log_handler = logging.StreamHandler()
_log_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)
_log.addHandler(_log_handler)
_log.setLevel("INFO")

class RandomButtonWin(QtWidgets.QMainWindow):
    def __init__(self, *args):
        '''
        Initialize the QMainWindow with a QPushButton
        '''
        super(RandomButtonWin, self).__init__(*args)

        # Set the name of our window
        self.setWindowTitle("Random Button Color UI")
        
        # Resize window 
        self.resize(500, 250)

        # Create button
        # The second arg here is the button's parent - self in this case (aka QMainWindow)
        self.run_btn = QtWidgets.QPushButton("Run", self)

        # Connect button so when it's pressed, it will change colors
        self.run_btn.pressed.connect(self.set_random_btn_color)

        # Testing logger
        # run_btn.released.connect(self.print_info)
    
    def set_random_btn_color(self):
        '''Set color button to random color'''

        # Generate set of random RGB values between 0 and 255
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        # Create a new palette that we'll apply to RandomButtonWin
        palette = QtGui.QPalette()

        # Set the button to the RGB value when the window is active
        self.run_btn.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")

        # Apply palette to the current RandomButtonWin() instance
        # self.setPalette(palette)

    
    def print_info(self):
        _log.info("Hello!")


if __name__ == "__main__":
    # Create a QApplication to handle our QMainWindow - needed for standalone application
    app = QtWidgets.QApplication(sys.argv)
    
    window = RandomButtonWin()

    window.show()

    # Execute the QApplication
    exit_code = app.exec_()
    sys.exit(exit_code)