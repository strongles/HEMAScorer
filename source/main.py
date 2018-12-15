import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QCheckBox, QHBoxLayout, QVBoxLayout, QAction, qApp
from PyQt5.QtCore import QSize


class ScorePanel(QVBoxLayout):
    def __init__(self, colour, parent):
        QVBoxLayout.__init__(self)
        self.bout_score_label = QLabel(str(0).rjust(2, "0"), parent)
        self.bout_score_label.setFont(QtGui.QFont("Digital-7", 200, QtGui.QFont.Bold))
        self.bout_score_label.setStyleSheet(f"background-color: {colour}")
        self.exchange_score_label = QLabel(str(0).rjust(2, "0"), parent)
        self.exchange_score_label.setFont(QtGui.QFont("Digital-7 Mono", 200, QtGui.QFont.Bold))
        self.exchange_score_label.setStyleSheet(f"background-color: {colour}")
        score_plus_button = QPushButton("+", parent)
        score_minus_button = QPushButton("-", parent)

        score_plus_button.clicked.connect(lambda: self.increment_label_score(self.exchange_score_label))
        score_minus_button.clicked.connect(lambda: self.decrement_label_score(self.exchange_score_label))
        button_layout = QHBoxLayout()
        self.addWidget(self.bout_score_label)
        self.addWidget(self.exchange_score_label)
        button_layout.addWidget(score_plus_button)
        button_layout.addWidget(score_minus_button)
        self.addLayout(button_layout)

    def add_exchange_score_to_bout_score(self):
        current_bout_total = int(self.bout_score_label.text())
        exchange_score = int(self.exchange_score_label.text())
        self.bout_score_label.setText(str(current_bout_total + exchange_score).rjust(2, "0"))
        self.exchange_score_label.setText(str(0).rjust(2, "0"))
        self.bout_score_label.repaint()
        self.exchange_score_label.repaint()

    def get_current_score(self):
        return int(self.bout_score_label.text())


    @staticmethod
    def increment_label_score(label):
        current_score = int(label.text())
        label.setText(str(current_score + 1).rjust(2, "0"))
        label.repaint()

    @staticmethod
    def decrement_label_score(label):
        current_score = int(label.text())
        label.setText(str(current_score - 1).rjust(2, "0"))
        label.repaint()


class ScorerWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("HEMAScorer")
        self.red_fencer_panel = None
        self.blue_fencer_panel = None
        self.score_double_box = None
        self.doubles_count = 0
        self.create_menus()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        central_widget.setLayout(self.construct_main_panel())

    def create_menus(self):
        """
        Menus for larger-scale operations
        - Setup of new pool
        - Connect to network of scoring machines on local network
        - "How to" section to train new users
        """
        self.statusBar().showMessage("Ready")
        extract_action = QAction("Exit", self)
        extract_action.setShortcut("Ctrl+Q")
        extract_action.setStatusTip('Leave The App')
        extract_action.triggered.connect(self.close_application)
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        file_menu.addAction(extract_action)

    @staticmethod
    def close_application():
        qApp.quit()

    def create_display(self):
        """
        Set up general display panel:
        - Initialise panel layout
        - Scoring panels (per competitor)
        - Bout listings
        - Timer panel
        """

    def construct_main_panel(self):
        """
        This will contain the information surrounding the scoring for both competitors
        """
        # red_fencer_panel = self.construct_scoring_panel("red")
        # blue_fencer_panel = self.construct_scoring_panel("blue")
        self.blue_fencer_panel = ScorePanel("blue", self)
        self.red_fencer_panel = ScorePanel("red", self)
        self.score_double_box = QCheckBox("Double", self)
        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.submit_exchange_score)
        undo_last_exchange_button = QPushButton("Undo Last", self)
        main_panel_layout = QHBoxLayout(self)
        main_panel_layout.addLayout(self.red_fencer_panel)
        main_panel_layout.addWidget(self.score_double_box)
        main_panel_layout.addLayout(self.blue_fencer_panel)
        main_panel_wrapper = QVBoxLayout(self)
        main_panel_wrapper.addLayout(main_panel_layout)
        main_panel_wrapper.addWidget(submit_button)
        main_panel_wrapper.addWidget(undo_last_exchange_button)
        return main_panel_wrapper

    def submit_exchange_score(self):
        self.blue_fencer_panel.add_exchange_score_to_bout_score()
        self.red_fencer_panel.add_exchange_score_to_bout_score()
        if self.score_double_box.isChecked():
            self.doubles_count += 1
            self.score_double_box.setChecked(False)
        if any([score >= 10 for score in [self.red_fencer_panel.get_current_score(), self.blue_fencer_panel.get_current_score()]]):
            print("A WINNER IS YOU")

    def construct_scoring_panel(self, competitor):
        """
        Set up a panel to:
        - Create a "current score" display
        - Create "exchange score" display
        - Create score modification buttons
          - Add
          - Subtract
        """
        bout_score_label = QLabel(str(0).rjust(2, "0"), self)
        bout_score_label.setFont(QtGui.QFont("Digital-7", 200, QtGui.QFont.Bold))
        bout_score_label.setStyleSheet(f"background-color: {competitor}")
        exchange_score_label = QLabel(str(0).rjust(2, "0"), self)
        exchange_score_label.setFont(QtGui.QFont("Digital-7 Mono", 200, QtGui.QFont.Bold))
        exchange_score_label.setStyleSheet(f"background-color: {competitor}")
        score_plus_button = QPushButton("+", self)
        score_minus_button = QPushButton("-", self)

        score_plus_button.clicked.connect(lambda: self.increment_label_score(exchange_score_label))
        score_minus_button.clicked.connect(lambda: self.decrement_label_score(exchange_score_label))
        scoring_layout = QVBoxLayout(self)
        button_layout = QHBoxLayout(self)
        scoring_layout.addWidget(bout_score_label)
        scoring_layout.addWidget(exchange_score_label)
        button_layout.addWidget(score_plus_button)
        button_layout.addWidget(score_minus_button)
        scoring_layout.addLayout(button_layout)
        return scoring_layout




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ScorerWindow()
    mainWin.show()
    sys.exit(app.exec_())
