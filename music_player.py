import vlc

class musicPlayer:
    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.url = None

    def play(self, url):
        """ Play Audio from the URL"""
        self.url = url
        media = self.instance.media_new(url)
        self.player.set_media(media)
        self.player.play()
    def pause(self):
        """ Pause Audio"""
        self.player.pause()
    def stop(self):
        """ Stop Audio"""
        self.player.stop()
    def is_playing(self):
        return self.player.is_playing()
    
    def get_position(self):
        return self.player.get_position()

