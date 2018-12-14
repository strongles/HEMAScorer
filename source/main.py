import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton
from PyQt5.QtCore import QSize


class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("Hello world")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)

        push_button = QPushButton(self)
        push_button.clicked.connect(self.button_action)
        push_button.resize(50, 50)
        push_button.move(50, 50)

        title = QLabel("Hello World from PyQt", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        grid_layout.addWidget(title, 0, 0)

    @staticmethod
    def button_action():
        print("Button clicked")

    def create_menus(self):
        """
        Menus for larger-scale operations
        - Setup of new pool
        - Connect to network of scoring machines on local network
        """

    def create_display(self):
        """
        Set up general display panel:
        - Initialise panel layout
        - Scoring panels (per competitor)
        - Bout listings
        - Timer panel
        """

    def construct_scoring_panel(self, competitor):
        """
        Set up a panel to:
        - Create a "current score" display
        - Create "exchange score" display
        - Create score modification buttons
          - Add
          - Subtract
          - Submit
          - Dismiss last score
        - "Double" checkbox
        - "No exchange" button?
        """


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit(app.exec_())
