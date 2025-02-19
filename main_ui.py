from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QSlider
from PyQt6.QtCore import Qt, QTimer

class mainUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YT Music Player")
        self.setGeometry(200,200,400,200)

        self.layout = QVBoxLayout()

        """Search input box."""
        self.search_box = QLineEdit(self)
        self.search_box.setPlaceholderText("Search for a song...")
        self.layout.addWidget(self.search_box)

        """Search and play button."""
        self.search_button = QPushButton("Search and Play", self)
        self.layout.addWidget(self.search_button)
        self.song_label = QLabel("Song will appear here", self)

        """Thumbnail"""
        self.thumbnail_label = QLabel(self)

        """Progress Bar"""
        self.progress_bar = QSlider(Qt.Orientation.Horizontal)
        self.progress_bar.setRange(0,100)
        self.progress_bar.sliderReleased.connect(self.seek_position)

        """Time to update progress bar"""
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)

        """Status"""
        self.status_label = QLabel("Ready")
        self.layout.addWidget(self.status_label)

        """Pause Button"""
        self.play_button = QPushButton("Pause/Play", self)
        self.layout.addWidget(self.play_button)


        layout = QVBoxLayout()
        layout.addWidget(self.search_box)
        layout.addWidget(self.search_button)
        layout.addWidget(self.thumbnail_label)
        layout.addWidget(self.song_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.play_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

