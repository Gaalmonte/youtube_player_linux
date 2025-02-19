import sys
from PyQt6.QtWidgets import QApplication
from ui_main import MainUI
from player import MusicPlayer
from youtube_api import search_song, get_audio_url

class YouTubeMusicApp(MainUI):
    def __init__(self):
        super().__init__()
        self.player = MusicPlayer()

        self.search_button.clicked.connect(self.search_and_play)
        self.play_button.clicked.connect(self.toggle_playback)

    def search_and_play(self):
        query = self.search_box.text()
        if not query:
            self.status_label.setText("Enter a song name!")
            return
        
        self.status_label.setText("Searching...")
        song = search_song(query)
        
        if not song:
            self.status_label.setText("No results found!")
            return

        video_id = song["videoId"]
        audio_url = get_audio_url(video_id)

        if not audio_url:
            self.status_label.setText("Failed to fetch audio!")
            return
        
        self.player.play(audio_url)
        self.status_label.setText(f"Playing: {song['title']}")

    def toggle_playback(self):
        if self.player.is_playing():
            self.player.pause()
            self.status_label.setText("Paused")
        else:
            self.player.play(self.player.url)
            self.status_label.setText("Playing")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeMusicApp()
    window.show()
    sys.exit(app.exec())
