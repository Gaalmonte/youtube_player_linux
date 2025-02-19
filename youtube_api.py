from ytmusicapi import YTMusic
import yt_dlp

ytmusic = YTMusic()

def search_song(query):
    """Search for a song on YouTube Music."""
    results = ytmusic.search(query, filter="songs")
    if results:
        return results[0]  # Return the first result
    return None

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
