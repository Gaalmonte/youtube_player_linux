from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel

class MainUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Music Desktop")
        self.setGeometry(200, 200, 400, 200)

        self.layout = QVBoxLayout()

        self.search_box = QLineEdit(self)
        self.search_box.setPlaceholderText("Search for a song...")
        self.layout.addWidget(self.search_box)

        self.search_button = QPushButton("Search & Play", self)
        self.layout.addWidget(self.search_button)

        self.status_label = QLabel("Ready")
        self.layout.addWidget(self.status_label)

        self.play_button = QPushButton("Pause", self)
        self.layout.addWidget(self.play_button)

        self.setLayout(self.layout)
