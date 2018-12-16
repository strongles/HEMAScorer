from scorelabel import ScoreLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton


class ScorePanel(QVBoxLayout):
    def __init__(self, colour, parent):
        super(ScorePanel, self).__init__()
        self.bout_score_label = ScoreLabel(colour, parent)
        self.exchange_score_label = ScoreLabel(colour, parent)
        self.score_history = []
        score_plus_button = QPushButton("+", parent)
        score_minus_button = QPushButton("-", parent)

        score_plus_button.clicked.connect(lambda: self.exchange_score_label.add_score(1))
        score_minus_button.clicked.connect(lambda: self.exchange_score_label.add_score(-1))
        button_layout = QHBoxLayout(parent)
        self.addWidget(self.bout_score_label)
        self.addWidget(self.exchange_score_label)
        button_layout.addWidget(score_plus_button)
        button_layout.addWidget(score_minus_button)
        self.addLayout(button_layout)

    def add_exchange_score_to_bout_score(self):
        current_bout_total = int(self.bout_score_label.text())
        exchange_score = int(self.exchange_score_label.text())
        self.score_history.append(exchange_score)
        self.bout_score_label.setText(str(current_bout_total + exchange_score).rjust(2, "0"))
        self.exchange_score_label.setText(str(0).rjust(2, "0"))
        self.bout_score_label.repaint()
        self.exchange_score_label.repaint()

    def get_current_score(self):
        return int(self.bout_score_label.text())

    def undo_last_score(self):
        if len(self.score_history) > 0:
            last_score = self.score_history[-1]
            self.score_history.pop(-1)
            current_bout_score = self.bout_score_label.get_score()
            self.bout_score_label.set_score(current_bout_score - last_score)

    @staticmethod
    def increment_score(label):
        current_score = int(label.text())
        label.setText(str(current_score + 1).rjust(2, "0"))
        label.repaint()

    @staticmethod
    def decrement_score(label):
        current_score = int(label.text())
        label.setText(str(current_score - 1).rjust(2, "0"))
        label.repaint()
