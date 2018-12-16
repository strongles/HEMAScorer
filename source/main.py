import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QCheckBox, QHBoxLayout, QVBoxLayout, QAction, qApp
from PyQt5.QtCore import QSize
from scorepanel import ScorePanel


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
        close_action = QAction("Exit", self)
        close_action.setShortcut("Ctrl+Q")
        close_action.setStatusTip('Leave The App')
        close_action.triggered.connect(self.close_application)
        connect_action = QAction("Connect", self)
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('&File')
        file_menu.addAction(connect_action)
        file_menu.addAction(close_action)

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
        undo_last_exchange_button.clicked.connect(self.undo_last_score)
        main_panel_layout = QHBoxLayout(self)
        main_panel_layout.addLayout(self.red_fencer_panel)
        main_panel_layout.addWidget(self.score_double_box)
        main_panel_layout.addLayout(self.blue_fencer_panel)
        main_panel_wrapper = QVBoxLayout(self)
        main_panel_wrapper.addLayout(main_panel_layout)
        main_panel_wrapper.addWidget(submit_button)
        main_panel_wrapper.addWidget(undo_last_exchange_button)
        return main_panel_wrapper

    def undo_last_score(self):
        self.red_fencer_panel.undo_last_score()
        self.blue_fencer_panel.undo_last_score()

    def submit_exchange_score(self):
        self.blue_fencer_panel.add_exchange_score_to_bout_score()
        self.red_fencer_panel.add_exchange_score_to_bout_score()
        if self.score_double_box.isChecked():
            self.doubles_count += 1
            self.score_double_box.setChecked(False)
        fencer_scores = {
            "red": self.red_fencer_panel.get_current_score(),
            "blue": self.blue_fencer_panel.get_current_score()
        }
        for fencer, score in fencer_scores.items():
            if score >= 10:
                print(f"{fencer} fencer wins - score cap reached.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = ScorerWindow()
    mainWin.show()
    sys.exit(app.exec_())
