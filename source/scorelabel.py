from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel, QSizePolicy


class ScoreLabel(QLabel):
    def __init__(self, colour, parent):
        super(ScoreLabel, self).__init__(parent)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored))
        self.setFont(QtGui.QFont("Digital-7 Mono", 200, QtGui.QFont.Bold))
        self.setStyleSheet(f"background-color: {colour}")
        self.set_score(str(0).rjust(2, "0"))

    def get_score(self):
        return int(self.text())

    def set_score(self, score):
        self.setText(str(score).rjust(2, "0"))
        self.repaint()

    def add_score(self, amount):
        current_score = self.get_score()
        self.set_score(current_score + amount)
