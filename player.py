import vlc

class MusicPlayer:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

    def play(self, url):
        """Play audio from the given URL."""
        media = self.instance.media_new(url)
        self.player.set_media(media)
        self.player.play()

    def pause(self):
        """Pause playback."""
        self.player.pause()

    def stop(self):
        """Stop playback."""
        self.player.stop()

    def is_playing(self):
        return self.player.is_playing()
