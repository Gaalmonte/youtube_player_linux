from ytmusicapi import YTMusic
import yt_dlp

ytmusic = YTMusic()

def search_song(self, query):
    """Search for a song on YouTube Music."""
    results = ytmusic.search(query, filter="songs")
    self.song_list.clear()
    self.songs = results

    print (f"Found {len(results)} songs")
    for song in results:
        print(f"{song['title']}")
        self.song_list.addItem(song["title"])
    # if results:
    #     return results[0]  # Return the first result
    # return None

def get_audio_url(video_id):
    """Extract direct audio URL using yt-dlp."""
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "extract_flat": True,
    }


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"https://music.youtube.com/watch?v={video_id}", download=False)
        return info["url"] if "url" in info else None
