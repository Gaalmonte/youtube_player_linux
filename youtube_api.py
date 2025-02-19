from ytmusicapi import YTMusic, OAuthCredentials
import yt_dlp

ytmusic = YTMusic("oauth.json","117715915696164247781", oauth_credentials=OAuthCredentials(client_id="977492998858-d0salhc8c3i71oe6jit1kgbfot8s1m0c.apps.googleusercontent.com", client_secret="977492998858-d0salhc8c3i71oe6jit1kgbfot8s1m0c.apps.googleusercontent.com"))

def search_song(query):
    """Search for a song on YT"""
    results = ytmusic.search(query, filter="songs")
    if not results:
        print("No search results found.")
        return None
    return results[0]

def grab_thumbnail(query):
    """Search for a song on YT and return the thumbnail URL"""
    results = ytmusic.search(query, filter="songs")
    if not results:
        print("No search results found.")
        return None
    song_data = results[0]
    # Safely return the thumbnail URL
    return song_data.get('thumbnails', [{}])[-1].get('url', '')  # Directly return URL

def get_audio_url(video_id):
    """Grabs direct audio URL using yt_dlp"""
    ydl_opts = {
        "format":"bestaudio/best",
        "quiet":True,
        "extract_flat":True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"https://music.youtube.com/watch?v={video_id}", download=False)
        return info["url"] if "url" in info else None