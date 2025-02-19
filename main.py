from io import BytesIO
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import requests
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

    def play_selected_song(self, item):
        """Play the selected song and update the thumbnail."""
        selected_index = self.song_list.row(item)
        selected_song = self.songs[selected_index]
        video_id = selected_song["videoId"]
        print(f"Playing: {selected_song['title']} (ID: {video_id})")
        # Fetch and update the song thumbnail
        self.update_thumbnail(video_id)

        # Get stream URL and play song
        self.play_song(video_id)    

    def update_thumbnail(self, video_id):
        """Fetch and display the thumbnail of the song."""
        song_info = self.ytmusic.get_song(video_id)
        thumbnail_url = song_info["thumbnails"][-1]["url"]
        print(f"Thumbnail URL: {thumbnail_url}")
        # Download and display the image
        response = requests.get(thumbnail_url)
        if response.status_code == 200:
            image = QPixmap()
            image.loadFromData(BytesIO(response.content).read())
            self.thumbnail_label.setFixedSize(200,200)
            self.thumbnail_label.setStyleSheet("border: 1px solid black;")
            self.thumbnail_label.setPixmap(image)
            self.thumbnail_label.setScaledContents(True)  # Adjust size
        else:
            print("Failed to load thumbnail.")    
        
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
