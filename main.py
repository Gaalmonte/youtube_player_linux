import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPixmap
import requests
from main_ui import mainUI
from music_player import musicPlayer
from youtube_api import search_song, get_audio_url, grab_thumbnail

class MusicApp(mainUI):
    def __init__(self):
        super().__init__()
        self.player = musicPlayer()

        # Connect buttons to their respective methods
        self.search_button.clicked.connect(self.search_and_play)
        self.play_button.clicked.connect(self.toggle_playback)

    def search_and_play(self):
        query = self.search_box.text()
        if not query:
            self.status_label.setText("Enter the song name:")
            return
            
        self.status_label.setText("Searching...")
        song = search_song(query)

        if not song:
            self.status_label.setText("No results found!")
            return

        # Safely get videoId and thumbnail
        video_id = song.get("videoId", None)
        
        thumbnail_url = grab_thumbnail(query)
        if not thumbnail_url:
            self.thumbnail_label.setText("No thumbnails found!")
            return
        
        if not video_id:
            self.status_label.setText("No video ID found!")
            return
        
        audio_url = get_audio_url(video_id)
        
        if not audio_url:
            self.status_label.setText("Failed to fetch audio!")
            return
        
        # Start playing the song
        self.player.play(audio_url)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(1000)  # Update every second

        self.song_label.setText(f"Currently Playing: {song['title']}")

        # Update the thumbnail if available
        if thumbnail_url:
            try:
                pixmap = QPixmap()
                pixmap.loadFromData(requests.get(thumbnail_url).content)
                self.thumbnail_label.setPixmap(pixmap.scaled(120, 120))
            except Exception as e:
                print(f"Error loading thumbnail: {e}")
                self.thumbnail_label.clear()  # Clear thumbnail if error occurs


    def toggle_playback(self):
        if self.player.is_playing():
            self.player.pause()
            self.timer.stop()
            self.status_label.setText("Paused.")
        else:
            self.player.play(self.player.url)  # Make sure this plays the correct URL
            self.timer.start(1000)
            self.status_label.setText("Playing.")

    def update_progress(self):
        position = self.player.get_position()
        
        if position >= 0:  # Ensure valid position
            print(f"Updating progress: {position}")
            self.progress_bar.setValue(int(position * 100))

    def seek_position(self):
        new_pos = self.progress_bar.value() / 100
        self.player.set_position(new_pos)  # Set the position for the audio

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicApp()
    window.show()
    sys.exit(app.exec())
